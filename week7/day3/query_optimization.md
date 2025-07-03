## What is Query Optimization in Django?

When Django interacts with the database (like PostgreSQL, MySQL, SQLite), it writes and runs **SQL queries** in the background.
But sometimes, **too many queries** are run — which **slows down your app**.

> Query Optimization is the process of reducing the number of database queries and making them faster.

---

## Why Optimize Queries?

Imagine you have:

* A `Student` model
* A `Department` model
  Each student belongs to a department.

If you show a list of students with department names, and you don't optimize your query — Django may run **1 query for students + 1 query for each student's department**.

That's called the **N+1 problem**, where `N` is the number of related objects.

> Result: Slow page load and poor performance.

---

## Solution: `select_related()` and `prefetch_related()`

These two methods help avoid the **N+1 query problem** and make your queries efficient.

---

## `select_related()` – Works for ForeignKey & OneToOne

### Use when you're following a **single-valued** relation (e.g. ForeignKey)

It performs a **SQL JOIN** and fetches the related object **in the same query**.

### Example

```python
# models.py
class Department(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
```

```python
# Without optimization
students = Student.objects.all()
for student in students:
    print(student.name, student.department.name)
```

This will run **1 query for students + 1 query per student for department**.

```python
# With select_related
students = Student.objects.select_related('department')
for student in students:
    print(student.name, student.department.name)
```

This runs **1 single JOIN query** to get both students and their departments.

---

## `prefetch_related()` – Works for ManyToMany & Reverse ForeignKey

### Use when you're dealing with **multi-valued** relationships (e.g. ManyToMany or reverse FK)

It performs **two queries**:

1. First for the main model
2. Second for the related model
   Then Django **joins them in Python memory**.

### Example

```python
# models.py
class Course(models.Model):
    name = models.CharField(max_length=100)

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)
```

```python
# Without optimization
teachers = Teacher.objects.all()
for teacher in teachers:
    for course in teacher.courses.all():
        print(teacher.name, course.name)
```

This will run **1 query for teachers + 1 query per teacher for courses**.

```python
# With prefetch_related
teachers = Teacher.objects.prefetch_related('courses')
for teacher in teachers:
    for course in teacher.courses.all():
        print(teacher.name, course.name)
```

This runs **2 total queries**, regardless of how many teachers there are.

---

## Comparison

| Feature           | `select_related`         | `prefetch_related`              |
| ----------------- | ------------------------ | ------------------------------- |
| Relationship Type | ForeignKey, OneToOne     | ManyToMany, Reverse FK          |
| Joins done in     | SQL (JOIN)               | Python (after separate queries) |
| Number of Queries | 1                        | 2 (usually)                     |
| Performance       | Faster for single object | Better for multiple objects     |

---

## When NOT to use them?

* If you're **not accessing related fields**, there's no benefit.
* Using `select_related` on **ManyToMany** will **fail**.
* Using `prefetch_related` on huge data may use more memory.

---

## How to Check Queries?

```python
from django.db import connection
print(connection.queries)
```

Or use **Django Debug Toolbar** for automatic tracking.

---

## Final Tips

* Use `select_related()` for single-valued relationships.
* Use `prefetch_related()` for many-valued relationships.
* Combine them if needed:

```python
Student.objects.select_related('department').prefetch_related('courses')
```

---

| Term               | Use For                 | Queries Made | Optimization Style |
| ------------------ | ----------------------- | ------------ | ------------------ |
| `select_related`   | ForeignKey / OneToOne   | 1            | SQL JOIN           |
| `prefetch_related` | ManyToMany / reverse FK | 2            | Python JOIN        |

---

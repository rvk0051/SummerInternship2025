## What is Redis?

Redis (REmote DIctionary Server) is:
- An in-memory data store
- Key-value based
- Extremely fast
- Supports complex data types: strings, hashes, lists, sets, sorted sets

Use cases:
- Caching
- Session storage
- Queues (Pub/Sub)
- Leaderboards, etc.

---

## Redis as a Cache

### Key Concepts:
- **TTL (Time to Live):** Auto-expiry of keys
- **Eviction Policy:** What happens when Redis memory is full (e.g., LRU)
- **Persistence:** Optionally persist data to disk

### Benefits:
- Fast data retrieval
- Reduces load on DB
- Ideal for session and page caching

---

## Why Use Redis with Django?

Django has a caching framework. Redis can act as the **backend** for it.
- Built-in support via `django-redis`
- Compatible with Django's `cache` API
- Works for:
  - Per-view cache (`@cache_page`)
  - Low-level API (`cache.set()`, `cache.get()`)

---

## Advantages of Using Redis for Caching:
- **Extremely Fast:** Its in-memory nature and optimized C code make it incredibly performant.

- **Simple to Use:** The key-value model and straightforward commands are easy to learn and implement.

- **Versatile:** Supports various data structures, fitting diverse caching needs.

- **Widely Adopted:** Large community, extensive documentation, and many client libraries for various programming languages.

- **Feature-Rich:** TTL, persistence, transactions, and pub/sub add to its power.

## Disadvantages/Considerations:
- **Memory Consumption:** Since data is in memory, the amount of data you can cache is limited by the available RAM on your Redis server.

- **Data Durability (for pure caching):** If Redis isn't configured for persistence, a server crash means all cached data is lost. For pure caching, this is often acceptable as the primary data source still holds the true data.

- **Cold Start:** After a restart or if the cache is empty, there will be a period of "cache misses" where the application has to fetch data from the slower primary source.

- **Complexity of Cache Invalidation:** While Redis makes it easy to set TTL, figuring out a robust strategy for invalidating data when the primary source changes can be complex, especially in distributed systems.

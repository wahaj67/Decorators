# 🚀 Python Decorators Toolkit

This project demonstrates a collection of custom Python decorators that showcase essential software engineering principles like modularity, performance analysis, debugging, and caching.

## 📚 Decorators Included

1. @timer

Measures how long a function takes to execute. Ideal for profiling.

2. @debug

Logs function name, arguments, and keyword arguments for better traceability.

3. @cache

Caches the result of expensive function calls to improve performance.

## 📦 Example Usage
@timer
def example(n):
    time.sleep(n)
    return "Done"

@debug
def add(n1, n2):
    return n1 + n2

@cache
def check(a, b):
    time.sleep(5)
    return a + b

## 🧠 Concepts Covered

Functional Programming

Decorators & Closures

Memoization

Logging

Performance Profiling

## 👤 Author

Wahaj Ali
COO @ Hashkoders
🌐 https://hashkoders.com

## 🤝 Contribute

PRs are welcome. Let’s build this into a go-to decorator library for real-world devs.

## 📜 License

This project is open-source under the MIT License.



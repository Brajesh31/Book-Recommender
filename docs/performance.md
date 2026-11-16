# 🚀 Performance and Resource Considerations

## Current runtime profile
The app loads four pickle artifacts when `app.py` is imported. This shifts loading cost to process startup and keeps data in memory for request handling. There is no cache service or database query path.

## Main resource drivers
- Size of the pivot table and similarity matrix.
- Number of WSGI worker processes.
- Pandas and NumPy object overhead.
- Sorting the full similarity row for each request.
- External cover-image latency in the visitor's browser.

## Practical deployment guidance
- Measure resident memory after loading the complete artifacts.
- Select worker count based on memory, not CPU count alone.
- Avoid loading a second artifact copy unnecessarily.
- Measure recommendation latency with representative titles.
- Consider partial top-K selection only after preserving exact result semantics and testing it.
- Consider image proxying/caching only after reviewing image rights and third-party terms.

## Measurement plan
Record environment, artifact dimensions, worker count, cold-start time, memory per worker, median and tail request latency, and concurrency. No benchmark numbers are currently published; do not invent them.

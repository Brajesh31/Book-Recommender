# 📘 Glossary

| Term | Meaning in this project |
|---|---|
| Artifact | A generated pickle file loaded by the Flask app |
| Book metadata | Title, author, publication fields, and cover URL |
| Collaborative filtering | Recommendation approach using patterns in user-item interactions |
| Cosine similarity | Similarity measure used by the notebook to compare book rating vectors |
| Cold start | Lack of sufficient interaction history for a new user or item |
| Git LFS | Git extension used to store large files outside ordinary Git blobs |
| Inference | Producing recommendations from an already prepared model |
| Item-item similarity | Similarity between book vectors in the rating pivot table |
| Jinja | Template engine used by Flask to render HTML |
| Pivot table | User-by-title matrix of rating values |
| Popularity ranking | List generated from rating counts and average ratings |
| Pickle | Python object serialization format; unsafe for untrusted input |
| WSGI | Python web-server interface used by servers such as Gunicorn |
| Model build | One consistent training/export run producing all related artifacts |
| Artifact alignment | Requirement that similarity matrix row positions correspond to pivot index positions |

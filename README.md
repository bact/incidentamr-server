# incidentamr-server

A server to test parsing text to Abstract Meaning Representation.

- Use [AMRLib](https://github.com/bjascob/amrlib) for AMR parsing, with a Sentence to Graph model from [amrlib-models](https://github.com/bjascob/amrlib-models)  (AMR is a graph, rather than a tree)
- Use [FastAPI](https://fastapi.tiangolo.com/) for server

## Install

1.  Download source
    ```sh
    git clone https://github.com/bact/incidentamr-server.git
    ```
2.  Install required libraries
    ```sh
    cd incidentamr-server
    pip install -r requirements.txt
    ```
3.  Install model
    - Download any *Sentence to Graph* model from [amrlib-models/releases](https://github.com/bjascob/amrlib-models/releases).
        - For example,  `model_parse_xfm_bart_large-v0_1_0.tar.gz`.
    - Extract the tar.gz file, you will get a directory containing .json and .bin files. Rename that directory to `stog`.
    - Put the `stog` directory inside `incidentamr-server/incidentamr_server/models` directory.


## Run

From inside `incidentamr_server` directory, run:

```sh
uvicorn main:app --reload
```

From within a web browser, open [http://127.0.0.1:8000](http://127.0.0.1:8000).

The web interface will look like this:

![IncidentAMR web interface](incidentamr-webpage.png)

from typing import List, Union

import amrlib
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


class Text(BaseModel):
    text: str


class AMRGraphs(BaseModel):
    graphs: List[str] = []


stog = amrlib.load_stog_model(model_dir="models/stog")

app = FastAPI()
templates = Jinja2Templates(directory="templates/")


#@app.get("/")
#def read_root():
#    return {"Hello": "World"}


@app.post("/parse/")
async def parse(text: Text):
    graphs = stog.parse_sents([text.text], add_metadata=False)
    amr = AMRGraphs()
    for graph in graphs:
        amr.graphs.append(str(graph))
    return amr


@app.get("/")
def form_post(request: Request):
    result = ""
    return templates.TemplateResponse("form.html", context={"request": request, "result": result})


@app.post("/")
def form_post(request: Request, text: str = Form(...)):
    graphs = stog.parse_sents([text], add_metadata=True)
    result = ""
    for graph in graphs:
        _text = str(graph)
        result = result + _text
    return templates.TemplateResponse("form.html", context={"request": request, "result": result})

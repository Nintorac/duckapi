from typing import List
import duckdb
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import Response
from pydantic import BaseModel, TypeAdapter

app = FastAPI()

class GroupEventValue(BaseModel):
    group_id: str
    event_value: int

Entries = List[GroupEventValue]
entries_adapter = TypeAdapter(Entries)

@app.post("/analyse_data/")
async def analyse_data(entries: Entries):
    
    if len(entries)==0:
        return []
    
    # Run the datapipeline over the list of entries
    group_event_values_df = pd.DataFrame(entries_adapter.dump_python(entries))
     
    duck = duckdb.connect('dev.duckdb')
    t = duck.begin()
    result = t.query('create or replace view group_event_values as \
        select group_id, event_value::int event_value from group_event_values_df')
    result = t.query('select * from analysis').to_df().to_json(orient='records')

    t.rollback() # roll back transaction to leave db in a good state

    return Response(content=str(result), media_type='application/json')

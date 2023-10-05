from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

# HTML form for feedback

@app.get("/", response_class=HTMLResponse)
def feedback_page():
    return feedback_form

# @app.post("/submit/", response_class=HTMLResponse)
# async def process_feedback(
#     name: str = Form(...),
#     email: str = Form(...),
#     message: str = Form(...),
# ):
    # You can process the feedback data here (e.g., save to a database)
    # For this example, we'll simply return a confirmation message
@app.post("/feedback/")
async def feedback_form(data: FormData):
    data_dict = data.dict()

    # Handle form data here
    print(data_dict)  # Print form data dictionary to the server console

    # Here you can save the data to a database (MongoDB in this case)
    myclient = pymongo.MongoClient("mongodb+srv://ipd:virat@ipd.bervskx.mongodb.net/")
    mydb = myclient["aagamhackthon"]
    mycol = mydb["feedback"]

    # Insert the data dictionary into the MongoDB collection
    mycol.insert_one(data_dict)
    return {"message": "Form submitted successfully!"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

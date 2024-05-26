from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import google.generativeai as genai

genai.configure(api_key="put your api key here")
# The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts

app = FastAPI()

def call_gemini_api(name: str, skills: str, goal: str):
    # Mock Gemini API response
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Provide response in HTML format . I am student i want you to create a roadmap for my career using my information. My name is : " + name + " . My skills are : " + skills + " . My goals are : " + goal + " . The result of this response would be directly rendered as html so give good html code with decent and professional css or styling")
    return response.parts[0].text

@app.get("/recommendation")
def get_recommendation(name: str, skills: str, goal: str):
    try:
        result = call_gemini_api(name, skills, goal)
        # return result
        return HTMLResponse(content=result, status_code=200)
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

from fastapi import FastAPI
from starlette.responses import RedirectResponse
from facebook_scraper import get_posts
from mongo_manager import *

app = FastAPI()

##get the root page request
@app.get("/root",summary="root page")
def root():
    return "Hello from the webscraper!"
    
##get the swagger doc
@app.get("/",include_in_schema=False)
async def redirect_to_swagger():
    return RedirectResponse(url='/docs')

##get the posts from facebook's page by its name and page's number
@app.get("/scrap/{page_name}/{pages_count}",summary="Scraps posts from facebook by page name and number of pages")
async def scrap_pages(page_name, pages_count):
    posts = []
    try:
        posts = list(get_posts(page_name, pages=int(pages_count)))
        posts = [delete_none(post) for post in posts]
        insert_posts(posts)
    except Exception as e:
        print(e)
    return posts

##get all scrapped posts in the database
@app.get("/read",summary="find all stored posts in database")
async def find_all():
    response = dict()
    posts = find_posts()
    response["total"] = len(posts)
    response["posts"] = posts
    return response

##get scrapped page in the database by its name
@app.get("/read/{page_name}",summary="find stored posts by page name in database")
async def find_by_name(page_name):
    response = dict()
    posts = find_posts(page_name)
    response["total"] = len(posts)
    response["posts"] = posts
    return response


def delete_none(d):
    new_dict = dict()
    for k, v in d.items():
        if v:
            new_dict[k] = v
    new_dict["_id"] = new_dict["post_id"]
    return new_dict
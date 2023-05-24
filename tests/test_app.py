from playwright.sync_api import Page, expect

# Tests for your routes go here


# ---------------Album tests ---------------

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/albums")
    h2_tags = page.locator("h2")
    expect(h2_tags).to_have_text([
        '\n            Doolittle\n        ', 
        '\n            Surfer Rosa\n        '
        ])
    paragraph_tags = page.locator("p")
    expect(paragraph_tags).to_have_text([
        '\n        Release year: 1989    \n        ', 
        '\n        Release year: 1988    \n        '
        ])

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Surfer Rosa")
    h1_tags = page.locator("h1")
    expect(h1_tags).to_have_text([
        '\n            Surfer Rosa\n        '
        ])
    release_tags = page.get_by_text('Release year:')
    expect(release_tags).to_have_text([
        '\n        Release year: 1988    \n        '
        ])
    artist_tag = page.get_by_text('Artist:')
    expect(artist_tag).to_have_text([
        '\n        Artist: Pixies    \n        '
        ])
    
def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/artists")
    h2_tags = page.locator('h2')
    expect(h2_tags).to_have_text(['Pixies'])
    p_tags = page.locator('p')
    expect(p_tags).to_have_text(['Genre: Rock'])

"""
We can create a new book and see it reflected in the list of books
"""
def test_create_album(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add new album'")
    
    page.fill("input[name=title]", "Test album")
    page.fill("input[name=release_year]", "1996")
    page.fill("input[name=artist_name]", "Jonny")

    page.click("text='Add album'")

    h1_tags = page.locator(".album-title")
    expect(h1_tags).to_have_text([ 'Test album'
        ])
    release_tags = page.get_by_text('Release year:')
    expect(release_tags).to_have_text([ 'Release year: 1996'
        ])
    artist_tag = page.locator('.artist-name')
    expect(artist_tag).to_have_text([
        'Artist: Jonny'
        ])
    
def test_validate_album(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add new album'")
    page.click("text='Add album'")

    errors_tag = page.locator(".t-errors")
    expect(errors_tag).to_have_text(
        "Your submission contains errors: " \
        "Title can't be blank" \
        "Release year can't be blank"
    )
    


# --------------- Artist tests ----------------------

def test_get_artist_by_click(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Pixies")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Pixies")
    genre_artist = page.get_by_text('Genre')
    expect(genre_artist).to_have_text('Genre: Rock')
    name_artist = page.get_by_text('Artist')
    expect(name_artist).to_have_text('Artist: Pixies')


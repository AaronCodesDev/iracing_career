from flet import Page, Text, app
from sqlalchemy import create_engine, text

# Probar Flet
def main(page: Page):
    page.add(Text("Flet funciona!"))

# Probar SQLAlchemy
engine = create_engine("sqlite:///test.db")
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY, name TEXT)"))
    conn.execute(text("INSERT INTO test(name) VALUES ('Aaron')"))
    conn.commit()
    result = conn.execute(text("SELECT * FROM test"))
    print(result.fetchall())

app(target=main)

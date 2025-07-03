from app.main import app  # Import your existing FastAPI app
from mangum import Mangum

# Create the Vercel handler
handler = Mangum(app)
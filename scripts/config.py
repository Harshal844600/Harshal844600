"""Everything personal lives here. Edit this file, re-run `python scripts/render_all.py`."""

USERNAME = "Harshal844600"
NAME = "Harshal Vidhate"
PROMPT_USER = "harshal"
PROMPT_HOST = "github"

# Cycled by the typing animation in header.svg
ROLES = [
    "Full Stack Developer (MERN Stack)",
    "DSA & Problem Solving Enthusiast",
    "Building AI-Driven Architectures",
    "Open for Internships & Full-Time Roles",
]

TAGLINE = "Pune, IN  ·  shipping full-stack products, AI systems & algorithms"

# neofetch-style rows on info-card.svg. "{...}" placeholders are filled from live data.
INFO_ROWS = [
    ("Role", "Full Stack Developer · Problem Solver"),
    ("Location", "Pune, Maharashtra, India"),
    ("Education", "Engineering Student"),
    ("Status", "Open to Internships & Opportunities"),
    ("Uptime", "{uptime} on GitHub"),
    ("Langs", "{top_langs}"),
    ("Frontend", "React · Next.js · TypeScript · Tailwind"),
    ("Backend", "Node.js · Express · Python · REST APIs"),
    ("Database", "MongoDB · PostgreSQL · Redis"),
    ("DSA", "LeetCode (ROY444704) · Graph & DP Solvers"),
    ("AI / ML", "Multimodal Assistive AI · Agent Architectures"),
    ("Repos", "{public_repos} public  ·  {stars} stars"),
    ("Activity", "{total} contributions this year"),
    ("Streak", "{current_streak}d current  ·  {longest_streak}d best"),
]

# globe.svg: home pin + arcs to the cloud regions you ship to (lat, lon)
HOME = ("Pune", 18.52, 73.85)
REGIONS = [
    ("ap-south-1", 19.08, 72.88),
    ("ap-southeast-1", 1.35, 103.82),
    ("eu-central-1", 50.11, 8.68),
    ("us-east-1", 38.95, -77.45),
    ("asia-northeast1", 35.68, 139.69),
]

# tech-sphere.svg: category -> labels (each category gets its own colour)
TECH = {
    "frontend": ["React", "Next.js", "TypeScript", "JavaScript", "Tailwind", "HTML5"],
    "backend": ["Node.js", "Express", "Python", "MongoDB", "REST APIs", "PostgreSQL"],
    "cloud": ["Docker", "AWS", "GitHub Actions", "Vercel", "Linux"],
    "ai": ["Multimodal AI", "LLM Agents", "Computer Vision", "Python"],
    "tools": ["Git", "GitHub", "Postman", "VS Code", "LeetCode"],
}

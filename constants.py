
tech_title_anchors = [
    "software engineer",
    "software developer",
    "backend engineer",
    "frontend engineer",
    "full-stack engineer",
    "systems engineer",
    "platform engineer",
    "site reliability engineer",
    "devops engineer",
    "cloud engineer",
    "infrastructure engineer",
    "application developer",
    "embedded software engineer",
    "mobile engineer",
    "data scientist",
    "data analyst",
    "machine learning engineer",
    "ai engineer",
    "applied scientist",
    "research scientist",
    "data engineer",
    "business intelligence analyst",
    "ml research engineer",
    "deep learning engineer",
    "nlp engineer",
    "computer vision engineer",
    "mlops engineer",
    "cybersecurity engineer",
    "security analyst",
    "security engineer",
    "information security engineer",
    "network engineer",
    "it support engineer",
    "systems administrator",
    "product manager",
    "technical program manager",
    "business analyst",
    "quantitative analyst",
    "data product manager",
    "operations analyst",
    "robotics engineer",
    "ar/vr engineer",
    "autonomous systems engineer",
    "simulation engineer",
    "blockchain engineer",
    "game developer",
    "cloud architect",
    "big data engineer"
]

# tech_title_anchors.extend([
#     # DevOps Engineer
#     "devops engineer",
#     "devops",
#     "devops developer",
#     "devops specialist",
#     "devops consultant",
#     "site reliability engineer",

#     # Infrastructure Engineer
#     "infrastructure engineer",
#     "systems engineer",
#     "platform engineer",
#     "it infrastructure engineer",
#     "network engineer",

#     # Application Developer
#     "application developer",
#     "app developer",
#     "mobile app developer",

#     # Cloud Engineer
#     "cloud engineer",
#     "cloud solutions engineer",
#     "cloud systems engineer",
#     "cloud developer",
#     "cloud infrastructure engineer",

#     # Platform Engineer
#     "platform engineer",
#     "platform developer",
#     "platform operations engineer",
#     "cloud platform engineer",

#     # Machine Learning Engineer
#     "machine learning engineer",
#     "ml engineer",
#     "ml developer",
#     "mlops engineer",
#     "ai engineer",

#     # IT Support Engineer
#     "it support engineer",
#     "it support specialist",
#     "desktop support engineer",
#     "technical support engineer",
#     "it helpdesk",

#     # Site Reliability Engineer
#     "site reliability engineer",
#     "sre",
#     "reliability engineer",
#     "cloud sre",

#     # Simulation Engineer
#     "simulation engineer",
#     "simulation software engineer",
#     "modeling engineer",
#     "simulation developer",

#     # Robotics Engineer
#     "robotics engineer",
#     "robotics software engineer",
#     "automation engineer",
#     "embedded robotics engineer",

#     # Backend Engineer
#     "backend engineer",
#     "backend developer",
#     "server-side engineer",
#     "api developer",
#     "backend software engineer",

#     # Mobile Engineer
#     "mobile engineer",
#     "mobile developer",
#     "android developer",
#     "ios developer",
#     "mobile app developer",

#     # Cybersecurity Engineer
#     "cybersecurity engineer",
#     "security engineer",
#     "information security engineer",
#     "it security engineer",
#     "cybersecurity analyst",

#     # Computer Vision Engineer
#     "computer vision engineer",
#     "cv engineer",
#     "image processing engineer",
#     "computer vision developer",

#     # AI Engineer
#     "artificial intelligence engineer",
#     "applied ai engineer",

#     # Full-Stack Engineer
#     "full-stack engineer",
#     "full stack developer",
#     "full-stack developer",

#     # Cloud Architect
#     "cloud architect",
#     "cloud solutions architect",
#     "cloud infrastructure architect",
#     "cloud system architect",

#     # Game Developer
#     "game developer",
#     "game programmer",
#     "unity developer",
#     "unreal engine developer",
#     "game software engineer",

#     # Applied Scientist
#     "applied scientist",
#     "ml researcher",
#     "ai researcher",
#     "research scientist ml",

#     # Frontend Engineer
#     "frontend engineer",
#     "frontend developer",
#     "ui engineer",
#     "web frontend developer",
#     "react developer",
#     "angular developer"])


import json

with open("../skill_mappings/skill_mapping.json", "r") as f:
    BASIC_SKILLS = json.load(f)

print("Loaded keys:", len(BASIC_SKILLS))
print(BASIC_SKILLS)

with open("../skill_mappings/additional_mapping.json", "r") as f: 
    BASIC_AND_ADDITIONAL_SKILLS = json.load(f)

print("Loaded keys:", len(BASIC_AND_ADDITIONAL_SKILLS))
print(BASIC_AND_ADDITIONAL_SKILLS)

with open("../skill_mappings/education_degree_mapping.json", "r") as f:
    EDUCATION_SKILLS = json.load(f)

print("Loaded keys:", len(EDUCATION_SKILLS))
print(EDUCATION_SKILLS)

with open("../skill_mappings/broad_mapping.json", "r") as f:
    EXTENDED_MAPPING = json.load(f)

print("Loaded keys:", len(EXTENDED_MAPPING))
print(EXTENDED_MAPPING)

with open("../skill_mappings/non_relevant_mapping.json", "r") as f:
    NON_RELEVANT_SKILLS_MAPPING = json.load(f)

print("Loaded keys:", len(NON_RELEVANT_SKILLS_MAPPING))
print(NON_RELEVANT_SKILLS_MAPPING)

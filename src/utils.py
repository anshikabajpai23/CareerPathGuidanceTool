
import re
import constants
import pandas as pd
def canonicalize_skill(skill: str, mappings) -> str:
    skill_clean = skill.strip().lower()
    # --------------------------------------------------
    # 3. CUSTOM CANONICAL RULES FOR COMMON CS SKILLS
    # --------------------------------------------------

    if skill_clean in mappings:
        return mappings[skill_clean]

    return skill_clean


# --------------------------------------------------
# 4. APPLY TO DATASET (df_tech["job_skills"])
# --------------------------------------------------
def split_normalize_and_canonicalize(text):
    if not isinstance(text, str):
        print("Skills are not string")
        return []

    tokens = [t.strip() for t in text.split(",")]
    # print(tokens)
    cleaned = [canonicalize_skill(t,constants.BASIC_SKILLS) for t in tokens]

    # cleaned = [canonicalize_skill(t,constants.BASIC_AND_ADDITIONAL_SKILLS) for t in cleaned]

    cleaned = [canonicalize_skill(t,constants.EDUCATION_SKILLS) for t in cleaned]

    # cleaned = [canonicalize_skill(t,constants.EXTENDED_MAPPING) for t in cleaned]

    cleaned = [canonicalize_skill(t,constants.NON_RELEVANT_SKILLS_MAPPING) for t in cleaned]

    cleaned = sorted(set([c for c in cleaned if c]))
    return cleaned

def get_user_vector(skills,skills_df):
    user_skills=split_normalize_and_canonicalize(skills)
    print("User Skills:", user_skills)
    skill_cols = skills_df.columns.tolist()
    
    user_vector = pd.Series(0, index=skill_cols)
    for skill in user_skills:
        if skill in user_vector.index:
            # print(skill)
            user_vector[skill] = 1

    return user_vector, user_skills, skill_cols
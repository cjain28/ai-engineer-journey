job = [" FrontEnd Developer "," AI Engineer "," Backend Developer "]

cleaned = [njob.strip() for njob in job]
print(",".join(cleaned))
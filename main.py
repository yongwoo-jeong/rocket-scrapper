from extract_jobs import get_jobs as get_rocket_jobs
from save import save_to_file

rocketpunch_jobs = get_rocket_jobs()
save_to_file(rocketpunch_jobs) 

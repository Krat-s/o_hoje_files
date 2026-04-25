from fastapi import FastAPI
from Web.print_ad import run_print_ad
import Global.settings.settings as cfg # temporário

app = FastAPI()

@app.get("/print-ad")
def print_ad():
    run_print_ad(cfg.ad_2, cfg.ad_2_folder)
    print('Ad printed susssccessfully')
    return {"message": "Ad printed successfully"}
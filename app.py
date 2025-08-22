from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
    if (request.method == "post"):
        on_demand_hourly = request.form.get("on_demand_hourly")
        reserved_discoun_pct = request.form.get("reserved_discoun_pct")
        instances_total = request.form.get("instances_total")
        hours_per_month = request.form.get("hours_per_month")
        reserved_share_pct = request.form.get("reserved_share_pct")
        other_reserved_share_pct_input = request.form.get("other_reserved_share_pct_input")
        reserved_upfront_monthly = request.form.get("reserved_upfront_monthly")
        return render_template("index.html", 
                               on_demand_hourly=on_demand_hourly, 
                               reserved_discoun_pct=reserved_discoun_pct, 
                               instances_total=instances_total,
                               hours_per_month=hours_per_month,
                               reserved_share_pct=reserved_share_pct,
                               other_reserved_share_pct_input=other_reserved_share_pct_input,
                               reserved_upfront_monthly=reserved_upfront_monthly)
    return render_template('index.html')

if __name__ == '__main__':
    app.route(debug=True)
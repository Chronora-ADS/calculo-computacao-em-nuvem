from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = 'chave_aleatoria_muito_secreta_e_segura_muito_mesmo'

@app.route('/', methods=['GET', 'POST'])
def home():
    # Inicializa histórico na sessão
    if 'history' not in session:
        session['history'] = []
    
    # Processa o formulário quando enviado
    if request.method == 'POST':
        try:
            # Coleta dados do formulário
            on_demand_hourly = float(request.form['on_demand_hourly'])
            reserved_discount_pct = float(request.form['reserved_discount_pct'])
            instances_total = int(request.form['instances_total'])
            hours_per_month = int(request.form.get('hours_per_month', 730))
            reserved_upfront_monthly = float(request.form.get('reserved_upfront_monthly', 0))
            
            # Lida com porcentagem personalizada
            reserved_share_pct = request.form['reserved_share_pct']
            if reserved_share_pct == 'other':
                reserved_share_pct = float(request.form['other-input'])
            else:
                reserved_share_pct = float(reserved_share_pct)
            
            # Cálculos (usando as fórmulas da atividade)
            price_reserved_hourly = on_demand_hourly * (1 - reserved_discount_pct / 100)
            inst_reserved = round(instances_total * reserved_share_pct / 100)
            inst_ondemand = instances_total - inst_reserved
            
            cost_reserved = inst_reserved * (
                price_reserved_hourly * hours_per_month + 
                reserved_upfront_monthly
            )
            cost_ondemand = inst_ondemand * (on_demand_hourly * hours_per_month)
            cost_total = cost_reserved + cost_ondemand
            
            baseline = instances_total * on_demand_hourly * hours_per_month
            saving_abs = baseline - cost_total
            saving_pct = (saving_abs / baseline) * 100

            # Armazena no histórico
            calculation = {
                'on_demand_hourly': on_demand_hourly,
                'reserved_discount_pct': reserved_discount_pct,
                'instances_total': instances_total,
                'hours_per_month': hours_per_month,
                'reserved_share_pct': reserved_share_pct,
                'reserved_upfront_monthly': reserved_upfront_monthly,
                'baseline': baseline,
                'cost_total': cost_total,
                'saving_abs': saving_abs,
                'saving_pct': saving_pct,
                'timestamp': len(session['history']) + 1 
            }
            session['history'].append(calculation)
            session.modified = True
            return redirect(url_for('home'))
            
        except (ValueError, KeyError) as e:
            print(f"Erro no processamento: {e}")
    
    # Renderiza a página com histórico
    return render_template(
        'index.html', 
        history=session.get('history', [])
    )

if __name__ == '__main__':
    app.run(debug=True)
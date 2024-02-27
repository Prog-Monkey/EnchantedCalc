from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])


def index():
    if request.method == 'POST':
        prices = []
        quantities = []
        how_much_to_make = []
        for i in range(1, 6):
            prices.append(float(request.form[f"price_{i}"]))
            quantities.append(int(request.form[f"quantity_sold_{i}"]))
            how_much_to_make.append(float(request.form[f"how_much_to_make_{i}"]))

        item_profits = []
        item_material_costs = []
        item_sold_for = []
        total_profits = 0
        total_material_costs = 0
        total_sold_for = 0

        for i in range(5):
            total_price = prices[i] * quantities[i]
            total_cost = how_much_to_make[i] * quantities[i]
            item_profit = total_price - total_cost
            total_profits += item_profit
            total_material_costs += total_cost
            total_sold_for += total_price

            item_profits.append(item_profit)
            item_material_costs.append(total_cost)
            item_sold_for.append(total_price)

        num_products = 5
        return render_template('results.html',
                               num_products=num_products,
                               item_profits=item_profits,
                               item_material_costs=item_material_costs,
                               item_sold_for=item_sold_for,
                               quantities=quantities,
                               how_much_to_make=how_much_to_make,
                               total_profits=total_profits,
                               total_material_costs=total_material_costs,
                               total_sold_for=total_sold_for)

    return render_template('index.html', num_products=5)


if __name__ == '__main__':
    app.run()

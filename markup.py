from model_parameters import amenities, neighbourhood_names, property_types, room_types


def make_select_options(options_names, option_name_transformer=lambda x: x):
    return "\n".join([
        f"<option value=\"{option_name_transformer(options_name)}\">{options_name}</option>"
        for options_name in options_names
    ])


style = """
.body {
    display:flex;
    height:100%;
    width:100%;
    background-color: #ffec6c;
    overflow: hidden;
}

.form {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    border: 3px black groove;
    border-radius: 4px;
    padding: 5px;
    background-color: #ffe948;
}

.input {
    margin: 10px 0;
    padding: 0;
    width: 100%;
    text-align: start;
    display: flex;
    justify-content: space-between;
};
"""

index_html = f"""
<style>{style}</style>

<body class="body">
    <main style="margin: auto; display: flex; flex-direction: column; justify-content: center; align-items: center">
        <h3>Barcelona Apartment Rent Price Estimator</h3>
        <form action="/predict" method="POST" class="form">
            <label for="host_is_superhost" class="input">
                <span>Are you a superhost?</span>
                <input type="checkbox" name="host_is_superhost"/>
            </label>
            <label for="host_listings_count" class="input">
                <span>Number of apartments, you have for rental:</span>
                <input type="number" name="host_listings_count" required />
            </label>
            <label for="accommodates" class="input">
                <span>Number of apartment accommodates:</span>
                <input type="number" name="accommodates" required />
            </label>
            <label for="bathrooms" class="input">
                <span>Number of apartment bathrooms:</span>
                <input type="number" name="bathrooms" required />
            </label>
            <label for="bedrooms" class="input">
                <span>Number of apartment bedrooms:</span>
                <input type="number" name="bedrooms" required />
            </label>     
            <label for="beds" class="input">
                <span>Total number of apartment beds:</span>
                <input type="number" name="beds" required />
            </label>
            <label for="minimum_nights" class="input">
                <span>Minimal number of nights for rent:</span>
                <input type="number" name="minimum_nights" required />
            </label>                        
            <label for="neighbourhood" class="input">
                <span>Choose apartment neighbourhood:</span>
                <select name="neighbourhood" required>
                    {make_select_options(neighbourhood_names)}
                </select>
            </label>
            <label for="property_type" class="input">
                <span>Choose property type:</span>
                <select name="property_type" required>
                    {make_select_options(property_types)}
                </select>
            </label>
            <label for="room_type" class="input">
                <span>Choose room type:</span>
                <select name="room_type" required>
                    {make_select_options(room_types)}
                </select>
            </label>
            <label for="amenities" class="input">
                <span style="display: block">Choose available amenities:</span>
                <select name="amenities" multiple required>
                    {make_select_options(amenities, lambda x: "has_" + x)}
                </select>
            </label>
            <input type="submit" value="Calculate" class="input" style="text-align: center"/>
        </form>
        <h3>Estimated Price: $last_predicted_price $</h3>
    </main>
</body>
"""


def render_index(last_predicted_price=0):
    return index_html.replace("$last_predicted_price", "{:.2f}".format(last_predicted_price))
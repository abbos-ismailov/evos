def foods_sort(food_type):
    photo_id = ""
    food_type_new = ""
    if food_type == "Lavashlar":
        photo_id = "AgACAgIAAxkBAAIMEWUe6lh3rezJDSy6ODWTIF2isQEGAAKvzTEb3D7xSGWrrPJ7aTggAQADAgADeQADMAQ"
        food_type_new = "🌯 " + food_type
    
    elif food_type == "Xot-Doglar":
        photo_id = "AgACAgIAAxkBAAIMKGUe7Zgv-5diZj5o_Rhr33hR_xUoAAKyzTEb3D7xSG9uguUKkr1rAQADAgADeQADMAQ"
        food_type_new = "🌭 " + food_type
    
    elif food_type == "Pitsalar":
        photo_id = "AgACAgIAAxkBAAIMLGUe7flgy7d338dglYy5X9k8g7C1AALBzTEb3D7xSAENi4Up0MOUAQADAgADeQADMAQ"
        food_type_new = "🍕 " + food_type
    
    elif food_type == "Ichimliklar":
        photo_id = "AgACAgIAAxkBAAIMMGUe7jwXZTLZE9kw3Mnp_GZuPPkbAAKwzTEb3D7xSNha_4GIkmKeAQADAgADeQADMAQ"
        food_type_new = "🥤 " + food_type
    
    elif food_type == "Salatlar":
        photo_id = "AgACAgIAAxkBAAIMNmUe8ElUyVEV1vjs5u7miO9-1FKuAAILyzEbb6T4SHaGkmBs2mXcAQADAgADdwADMAQ"
        food_type_new = "🥗 " + food_type
    
    elif food_type == "Burgerlar":
        photo_id = "AgACAgIAAxkBAAIMOmUe8O3XaY0pEBkoGzgTZRtspnOhAALAzTEb3D7xSL5N39BlocXhAQADAgADeQADMAQ"
        food_type_new = "🍔 " + food_type
    return [photo_id, food_type_new]
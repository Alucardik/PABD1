from numpy import array, float32

amenities = [
    '24-hour_check-in', 'accessible-height_bed', 'accessible-height_toilet',
    'air_conditioning', 'air_purifier', 'alfresco_bathtub',
    'amazon_echo', 'baby_bath', 'baby_monitor',
    'babysitter_recommendations', 'balcony', 'bath_towel',
    'bathroom_essentials','bathtub', 'bathtub_with_bath_chair',
    'bbq_grill', 'beach_essentials','beach_view',
    'beachfront', 'bed_linens', 'bedroom_comforts',
    'bidet', 'body_soap', 'breakfast',
    'breakfast_table', 'building_staff', 'buzzer/wireless_intercom',
    'cable_tv', 'carbon_monoxide_detector', 'cat(s)',
    'ceiling_fan', 'central_air_conditioning', 'changing_table',
    'children’s_books_and_toys', 'children’s_dinnerware', 'cleaning_before_checkout',
    'coffee_maker', 'convection_oven', 'cooking_basics',
    'crib', 'day_bed', 'disabled_parking_spot',
    'dishes_and_silverware', 'dishwasher', 'dog(s)',
    'doorman', 'double_oven', 'dryer',
    'dvd_player', 'electric_profiling_bed', 'elevator',
    'en_suite_bathroom', 'espresso_machine', 'essentials',
    'ethernet_connection', 'ev_charger', 'exercise_equipment',
    'extra_pillows_and_blankets', 'extra_space_around_bed', 'family/kid_friendly',
    'fax_machine', 'fire_extinguisher', 'fireplace_guards',
    'firm_mattress', 'first_aid_kit', 'fixed_grab_bars_for_shower',
    'fixed_grab_bars_for_toilet', 'flat_path_to_guest_entrance', 'formal_dining_area',
    'free_parking_on_premises', 'free_street_parking', 'full_kitchen',
    'game_console', 'garden_or_backyard', 'gas_oven',
    'ground_floor_access', 'gym', 'hair_dryer',
    'hammock', 'handheld_shower_head', 'hangers',
    'hbo_go', 'heat_lamps', 'heated_floors',
    'heated_towel_rack', 'heating', 'high-resolution_computer_monitor',
    'high_chair', 'host_greets_you', 'hot_tub',
    'hot_water', 'hot_water_kettle', 'indoor_fireplace',
    'internet', 'iron', 'jetted_tub',
    'keypad', 'kitchen', 'kitchenette',
    'lake_access', 'laptop_friendly_workspace', 'lock_on_bedroom_door',
    'lockbox', 'long_term_stays_allowed', 'luggage_dropoff_allowed',
    'memory_foam_mattress', 'microwave', 'mini_fridge',
    'mobile_hoist', 'mountain_view', 'mudroom',
    'murphy_bed', 'netflix', 'no_stairs_or_steps_to_enter',
    'other', 'other_pet(s)', 'outdoor_kitchen',
    'outdoor_parking', 'outdoor_seating', 'outlet_covers',
    'oven', 'pack_’n_play/travel_crib', 'paid_parking_off_premises',
    'paid_parking_on_premises', 'patio_or_balcony', 'pets_allowed',
    'pets_live_on_this_property', 'pillow-top_mattress', 'pocket_wifi',
    'pool', 'pool_cover', 'pool_with_pool_hoist',
    'printer', 'private_bathroom', 'private_entrance',
    'private_hot_tub', 'private_living_room', 'projector_and_screen',
    'rain_shower', 'refrigerator', 'roll-in_shower',
    'room-darkening_shades', 'safety_card', 'sauna',
    'self_check-in', 'shampoo', 'shared_gym',
    'shared_pool', 'shower_chair', 'single_level_home',
    'ski-in/ski-out', 'smart_lock', 'smart_tv',
    'smoke_detector', 'smoking_allowed', 'soaking_tub',
    'sound_system', 'stair_gates', 'standing_valet',
    'steam_oven', 'stove', 'suitable_for_events',
    'sun_loungers', 'table_corner_guards', 'tennis_court',
    'terrace', 'toilet', 'toilet_paper',
    'touchless_faucets', 'tv', 'walk-in_shower',
    'warming_drawer', 'washer', 'washer_/_dryer',
    'waterfront', 'well-lit_path_to_entrance','wheelchair_accessible',
    'wide_clearance_to_shower', 'wide_doorway_to_guest_bathroom', 'wide_entrance',
    'wide_entrance_for_guests', 'wide_entryway', 'wide_hallways',
    'wifi', 'window_guards',
]

neighbourhood_names = [
    'Sant Martí', 'La Sagrada Família', 'Vila de Gràcia',
    'Horta-Guinardó', "Camp d'en Grassot i Gràcia Nova", 'Gràcia',
    'Les Corts', 'El Gòtic', 'Ciutat Vella',
    'Eixample', "L'Antiga Esquerra de l'Eixample", 'La Barceloneta',
    'El Poble-sec', 'El Raval', 'Sants-Montjuïc',
    'El Clot', 'Sant Antoni', 'Diagonal Mar - La Mar Bella',
    'El Poblenou', "Dreta de l'Eixample", 'El Besòs i el Maresme',
    "La Nova Esquerra de l'Eixample", 'La Salut',
    'Sant Pere/Santa Caterina', 'Vallcarca i els Penitents',
    'el Fort Pienc', 'Sant Gervasi - Galvany',
    'Sant Martí de Provençals', "El Camp de l'Arpa del Clot", 'Sarrià',
    'La Vila Olímpica', 'Vilapicina i la Torre Llobeta', 'El Born',
    'Sarrià-Sant Gervasi', 'Glòries - El Parc', 'Sant Andreu',
    'El Baix Guinardó', 'Nou Barris', 'El Putget i Farró',
    'La Prosperitat', "La Font d'en Fargues", 'Horta',
    'La Maternitat i Sant Ramon', 'Provençals del Poblenou',
    'La Sagrera', 'Sant Gervasi - la Bonanova',
    'La Guineueta - Canyelles', 'La Teixonera', 'Can Baro', 'Navas',
    'Sant Andreu de Palomar', 'El Coll', 'Guinardó', 'Carmel',
    'La Verneda i La Pau', 'El Congrés i els Indians',
    'Les Tres Torres', 'Turó de la Peira - Can Peguera', 'Montbau',
    "La Vall d'Hebron", 'Sant Genís dels Agudells', 'El Bon Pastor',
    'Verdum - Los Roquetes', 'Pedralbes', 'Porta', 'Trinitat Nova',
    'La Trinitat Vella', 'Torre Baró',
]

property_types = [
    'Apartment', 'Loft', 'Bed and breakfast', 'Condominium',
    'Serviced apartment', 'Boat', 'Other', 'House', 'Aparthotel',
    'Guesthouse', 'Boutique hotel', 'Townhouse', 'Guest suite',
    'Hostel', 'Villa', 'Tiny house', 'Casa particular (Cuba)', 'Hotel',
    'Chalet', 'Dorm', 'Camper/RV', 'Cabin', 'Farm stay', 'Barn',
    'Dome house', 'Earth house', 'Cottage',
]

room_types = ['Entire home/apt', 'Private room', 'Shared room']

cat_cols = {"neighbourhood", "room_type", "property_type"}

numerical_cols = {
    "bedrooms",
    "accommodates",
    "bathrooms",
    "minimum_nights",
    "host_listings_count",
    "beds",
}


def wrap_num_param(param):
    return [[array(param, dtype=float32)]]


def wrap_cat_param(param):
    return [[param]]
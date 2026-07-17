from flask import g


def inject_globals():
    """
    Provides global context variables to all templates.
    """
    return {
        "current_user": getattr(g, "current_user", None),  # or current_user if using Flask-Login
        "cart_items": [],
        "admin": False

    }


def inject_dummy_products():
    """
    Provides dummy coffee products for testing templates before database is ready.
    """
    dummy_products = [
        {
            'id': 1,
            'name': 'Midnight Roast Espresso',
            'slug': 'midnight-roast-espresso',
            'image': 'https://media.istockphoto.com/id/1242525063/photo/fresh-coffee-beans-sourced-from-ethiopia.jpg?s=612x612&w=0&k=20&c=KUpRe3cDLI4uSY18Gr9vacoq0MJU3E5addOJVNwrozs=',
            '_avg_rating': 4.8,
            '_lowest_box': {'price_gbp_unit': 4.99},
            'is_active': True
        },
        {
            'id': 2,
            'name': 'Hazelnut Dream Cold Brew',
            'slug': 'hazelnut-dream-cold-brew',
            'image': 'https://media.istockphoto.com/id/1242525063/photo/fresh-coffee-beans-sourced-from-ethiopia.jpg?s=612x612&w=0&k=20&c=KUpRe3cDLI4uSY18Gr9vacoq0MJU3E5addOJVNwrozs=',
            '_avg_rating': 4.2,
            '_lowest_box': {'price_gbp_unit': 3.49},
            'is_active': True
        },
        {
            'id': 3,
            'name': 'Vanilla Bean Latte Blend',
            'slug': 'vanilla-bean-latte-blend',
            'image': 'https://media.istockphoto.com/id/1242525063/photo/fresh-coffee-beans-sourced-from-ethiopia.jpg?s=612x612&w=0&k=20&c=KUpRe3cDLI4uSY18Gr9vacoq0MJU3E5addOJVNwrozs=',
            '_avg_rating': 4.5,
            '_lowest_box': {'price_gbp_unit': 3.99},
            'is_active': True
        },
        {
            'id': 4,
            'name': 'Ethiopian Single Origin',
            'slug': 'ethiopian-single-origin',
            'image': 'https://media.istockphoto.com/id/1242525063/photo/fresh-coffee-beans-sourced-from-ethiopia.jpg?s=612x612&w=0&k=20&c=KUpRe3cDLI4uSY18Gr9vacoq0MJU3E5addOJVNwrozs=',
            '_avg_rating': 4.9,
            '_lowest_box': {'price_gbp_unit': 6.49},
            'is_active': True
        },
        {
            'id': 5,
            'name': 'Cinnamon Roll Blonde Roast',
            'slug': 'cinnamon-roll-blonde-roast',
            'image': 'https://media.istockphoto.com/id/1242525063/photo/fresh-coffee-beans-sourced-from-ethiopia.jpg?s=612x612&w=0&k=20&c=KUpRe3cDLI4uSY18Gr9vacoq0MJU3E5addOJVNwrozs=',
            '_avg_rating': 3.9,
            '_lowest_box': {'price_gbp_unit': 4.29},
            'is_active': True
        },
        {
            'id': 5,
            'name': 'Cinnamon Roll Blonde Roast',
            'slug': 'cinnamon-roll-blonde-roast',
            'image': 'https://media.istockphoto.com/id/1242525063/photo/fresh-coffee-beans-sourced-from-ethiopia.jpg?s=612x612&w=0&k=20&c=KUpRe3cDLI4uSY18Gr9vacoq0MJU3E5addOJVNwrozs=',
            '_avg_rating': 3.9,
            '_lowest_box': {'price_gbp_unit': 4.29},
            'is_active': True
        },
    ]
    return dict(dummy_products=dummy_products, user_alerts={})

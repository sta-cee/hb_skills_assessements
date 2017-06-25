"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# Datatype is query.

# >>> f = Brand.query.filter_by(name='Ford')
# >>> type(f)
# <class 'flask_sqlalchemy.BaseQuery'>
# >>> f = Brand.query.filter_by(name='Ford').all()
# >>> type(f)
# <type 'list'>

# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# An association table is a table that has no meaningful fields and simply
# serves as the glue between two tables. The naming convention is to name the
# association table after a combination of the two tables that it's connecting
# (ex: if the two tables are 'movie' and 'genre', the association table would
# be named MovieGenre (or GenreMovie). Association tables are a design decision
# that the database is not aware of.

# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = db.session.query(Brand).filter_by(brand_id='ram').all()

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = db.session.query(Model).filter_by(name='Corvette', brand_id='che').all()

# Get all models that are older than 1960.
q3 = db.session.query(Model).filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
q4 = db.session.query(Brand).filter(Brand.founded > 1920).all()

# Get all models with names that begin with ``Cor``.
q5 = db.session.query(Model).filter(Model.name.like('Cor%')).all()
# https://stackoverflow.com/questions/4926757/sqlalchemy-query-where-a-column-contains-a-substring

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = db.session.query(Brand).filter(Brand.founded == 1903, Brand.discontinued == None).all()
# https://stackoverflow.com/questions/5602918/select-null-values-in-sqlalchemy

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = db.session.query(Brand).filter((Brand.founded < 1950) | (Brand.discontinued != None)).all()
# https://stackoverflow.com/questions/7942547/using-or-in-sqlalchemy

# Get all models whose brand_id is not ``for``.
q8 = db.session.query(Model).filter(Model.brand_id != 'for').all()


# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    mdls = Model.query.options(db.joinedload('brand')).all()

    for mdl in mdls:
        if mdl.year == year:
            print '\nMODEL NAME: {}\n-----------\nYEAR: {}\nBRAND: {}\nHEADQUARTERS: {}\n'.format(mdl.name, mdl.year, mdl.brand.name, mdl.brand.headquarters)


def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    brnds = Brand.query.options(db.joinedload('model')).all()

    for brand in brnds:
        print '\nBRAND: {}\n{}\n'.format(brand.name, brand.model)


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    # Doesn't work unless you enter the string with the first letter capitalized .
    # Tried adding .lower() but that broke everything.

    brand_str = db.session.query(Brand).filter(Brand.name.like('%{}%'.format(mystr))).all()
    print brand_str


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    models_in_year_range = Model.query.filter(Model.year > int(start_year), Model.year < int(end_year)).all()

    for model in models_in_year_range:
        print model

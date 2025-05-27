# car_cli/cli.py
import click
from car_cli.database import db_session, init_db
from car_cli.models import Car


# Initialize DB on first run
init_db()


@click.group()
def cli():
    """🚗 Car Dealership CLI"""
    pass


@cli.command()
@click.option('--make', prompt='Make', help='Car make (e.g., Toyota)')
@click.option('--model', prompt='Model', help='Car model (e.g., Camry)')
@click.option('--year', prompt='Year', type=int, help='Manufacture year')
@click.option('--color', prompt='Color', help='Car color')
def add_car(make, model, year, color):
    """Add a new car."""
    new_car = Car(make=make, model=model, year=year, color=color)
    db_session.add(new_car)
    db_session.commit()
    click.echo(f"✅ Added {make} {model} ({year}, {color})")


@cli.command()
@click.argument('car_id', type=int)
@click.option('--make', help='New make of the car')
@click.option('--model', help='New model of the car')
@click.option('--year', type=int, help='New year of the car')
@click.option('--color', help='New color of the car')
def update_car(car_id, make, model, year, color):
    """Update an existing car by ID."""
    car = db_session.get(Car, car_id)
    if not car:
        click.echo(f"❌ No car found with ID {car_id}")
        return

    if make:
        car.make = make
    if model:
        car.model = model
    if year:
        car.year = year
    if color:
        car.color = color

    db_session.commit()
    click.echo(f"✅ Car ID {car_id} updated.")


@cli.command()
@click.argument('car_id', type=int)
def delete_car(car_id):
    """Delete a car by ID."""
    car = db_session.get(Car, car_id)
    if not car:
        click.echo(f"❌ No car found with ID {car_id}")
        return

    db_session.delete(car)
    db_session.commit()
    click.echo(f"🗑️ Car ID {car_id} deleted.")


if __name__ == '__main__':
    cli()
# seed.py
import logging
from car_cli.database import init_db, db_session
from car_cli.models import Car

def seed_database():
    # Initialize database
    init_db()

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('seed.log'),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger(__name__)

    # Sample cars data
    cars_data = [
    {'make': 'Toyota', 'model': 'Camry', 'year': 2022, 'color': 'Blue'},
    {'make': 'Honda', 'model': 'Civic', 'year': 2021, 'color': 'Red'},
    {'make': 'Ford', 'model': 'F-150', 'year': 2020, 'color': 'Black'},
    {'make': 'Tesla', 'model': 'Model S', 'year': 2023, 'color': 'White'},
    {'make': 'BYD', 'model': 'Seal', 'year': 2025, 'color': 'white'},
    {'make': 'hyundai', 'model': 'Tuscon', 'year': 2021, 'color': 'red'},
    {'make': 'nissan', 'model': 'x-trail', 'year': 2019, 'color': 'sky blue'},
    {'make': 'mercedes', 'model': 'C-class', 'year': 2024, 'color': 'blue'},
    {'make': 'honda', 'model': 'Civic', 'year': 2019, 'color': 'purple'},
    {'make': 'Ferrari', 'model': '296 GTB', 'year': 2023, 'color': 'grey'}
]
    
        
    

    try:
        logger.info("Starting database seeding...")
        
        # Check if cars already exist to prevent duplicates
        if db_session.query(Car).count() == 0:
            for car_info in cars_data:
                car = Car(**car_info)
                db_session.add(car)
            
            db_session.commit()
            logger.info("Successfully seeded database!")
            print("🌱 Database seeded successfully!")
        else:
            logger.info("Database already contains data - skipping seeding")
            print("✅ Database already seeded - no changes made")

    except Exception as e:
        logger.error(f"Error during seeding: {e}")
        db_session.rollback()
        print("❌ Error seeding database - check seed.log for details")
        raise

    finally:
        db_session.close()

if __name__ == "__main__":
    seed_database()
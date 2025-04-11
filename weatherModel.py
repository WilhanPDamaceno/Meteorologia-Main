from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./weatherModel.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class WeatherData(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(String)
    humidity = Column(String)
    AirPress = Column(String)
    WindVelocity = Column(String)
    WindDirection = Column(String)
    soilHumidity = Column(String)
    luminosity = Column(String)


Base.metadata.create_all(bind=engine)

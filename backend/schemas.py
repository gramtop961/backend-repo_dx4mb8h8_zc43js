"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

# Example schemas (you can keep these for reference):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in pounds")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# LandlordLink app schemas
# --------------------------------------------------

class Lead(BaseModel):
    """
    Leads generated from signup/cta forms
    Collection name: "lead"
    """
    name: str = Field(..., description="Full name of the lead")
    email: EmailStr = Field(..., description="Email address")
    company: Optional[str] = Field(None, description="Company or business name")
    portfolio_size: Optional[str] = Field(None, description="Number of units/properties managed")
    preference: Literal["trial", "demo"] = Field("trial", description="Whether user wants a trial or demo")
    message: Optional[str] = Field(None, description="Optional message from the lead")
    source: Optional[str] = Field(None, description="Where the lead came from (e.g., hero, mid-cta)")

class DemoRequest(BaseModel):
    """
    Demo requests (separate collection if needed)
    Collection name: "demorequest"
    """
    name: str
    email: EmailStr
    company: Optional[str] = None
    portfolio_size: Optional[str] = None
    message: Optional[str] = None
    source: Optional[str] = None

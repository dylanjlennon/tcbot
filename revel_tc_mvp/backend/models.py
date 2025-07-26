from pydantic import BaseModel, Field
from typing import List, Optional


class ContractData(BaseModel):
    """
    Represents the extracted data from a real estate contract.  In this MVP the
    fields are simplified.  Future versions should include contingencies,
    financing details, deadlines, and party information.
    """

    property_address: str = Field(..., description="Address of the property")
    buyer_name: str = Field(..., description="Name of the buyer")
    seller_name: str = Field(..., description="Name of the seller")
    closing_date: Optional[str] = Field(None, description="Proposed closing date (ISO format)")


class Transaction(BaseModel):
    """
    Represents a transaction record stored in the system.
    """

    id: int
    contract: ContractData
    status: str = Field("new", description="Status of the transaction (new, in_progress, closed)")


class TransactionCreate(BaseModel):
    """
    Request body schema for creating a transaction.  It embeds contract data
    extracted from an uploaded document.  In a more advanced version this
    endpoint would accept raw files and perform extraction.
    """

    contract: ContractData
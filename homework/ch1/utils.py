
from decimal import Decimal

def format_float2(x: float) -> str: 
	return f"{Decimal(x):.2E}"

def format_float3(x: float) -> str: 
	return f"{Decimal(x):.3E}"

def print_float3(message: str, x: float) -> None: 
	print(f"{message}: {format_float3(x)}")

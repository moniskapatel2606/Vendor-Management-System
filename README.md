# Vendor Management System with Performance Metrics

This project is a Vendor Management System built using Django and Django REST Framework. The system allows users to manage vendor profiles, track purchase orders, and calculate vendor performance metrics.

## Features

### Vendor Profile Management
- Users can create, retrieve, update, and delete vendor profiles.
- Each vendor profile includes essential information such as name, contact details, address, and a unique vendor code.

### Purchase Order Tracking
- Users can create, retrieve, update, and delete purchase orders.
- Purchase orders contain details such as PO number, vendor reference, order date, delivery date, items, quantity, and status.

### Vendor Performance Evaluation
- The system calculates and displays various performance metrics for vendors, including:
  - On-Time Delivery Rate
  - Quality Rating Average
  - Average Response Time
  - Fulfillment Rate

## Models

### Vendor Model
- Fields:
  - name (CharField)
  - contact_details (TextField)
  - address (TextField)
  - vendor_code (CharField, unique)
  - on_time_delivery_rate (FloatField)
  - quality_rating_avg (FloatField)
  - average_response_time (FloatField)
  - fulfillment_rate (FloatField)

### Purchase Order Model
- Fields:
  - po_number (CharField, unique)
  - vendor (ForeignKey to Vendor model)
  - order_date (DateTimeField)
  - delivery_date (DateTimeField)
  - items (JSONField)
  - quantity (IntegerField)
  - status (CharField)
  - quality_rating (FloatField, nullable)
  - issue_date (DateTimeField)
  - acknowledgment_date (DateTimeField, nullable)

### Historical Performance Model (Optional)
- Fields:
  - vendor (ForeignKey to Vendor model)
  - date (DateTimeField)
  - on_time_delivery_rate (FloatField)
  - quality_rating_avg (FloatField)
  - average_response_time (FloatField)
  - fulfillment_rate (FloatField)

## API Endpoints

### Vendor Endpoints
- `POST /api/vendors/`: Create a new vendor.
- `GET /api/vendors/`: List all vendors.
- `GET /api/vendors/{vendor_id}/`: Retrieve a specific vendor's details.
- `PUT /api/vendors/{vendor_id}/`: Update a vendor's details.
- `DELETE /api/vendors/{vendor_id}/`: Delete a vendor.

### Purchase Order Endpoints
- `POST /api/purchase_orders/`: Create a purchase order.
- `GET /api/purchase_orders/`: List all purchase orders.
- `GET /api/purchase_orders/{po_id}/`: Retrieve details of a specific purchase order.
- `PUT /api/purchase_orders/{po_id}/`: Update a purchase order.
- `DELETE /api/purchase_orders/{po_id}/`: Delete a purchase order.

### Vendor Performance Endpoint
- `GET /api/vendors/{vendor_id}/performance/`: Retrieve a vendor's performance metrics.

### Additional Endpoints
- `POST /api/purchase_orders/{po_id}/acknowledge/`: Endpoint for vendors to acknowledge purchase orders.

## Implementation

The project is implemented using Django and Django REST Framework.
- Models: Vendor, PurchaseOrder, HistoricalPerformance (optional)
- Views: Implemented using Django's generic views and Django REST Framework's API views.
- Serializers: Convert model instances to JSON format for API responses.
- URL Configuration: Maps API endpoints to their respective views.
- Business Logic: Backend logic implemented for calculating performance metrics and handling purchase order acknowledgment.
- Documentation: Thoroughly documented API endpoints, models, and features in this README file.

## Getting Started

To run the project locally, follow these steps:

### Prerequisites
- Python 3.x
- Django
- Django REST Framework

### Setup Instructions
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install dependencies using `pip install -r requirements.txt`.
4. Apply database migrations using `python manage.py migrate`.
5. Create a superuser to access the admin interface: `python manage.py createsuperuser`.
6. Start the development server: `python manage.py runserver`.
7. Access the API endpoints in your web browser or using tools like Postman.

## Testing

A comprehensive test suite is included to ensure the functionality and reliability of the API endpoints. To run the tests, use the following command:


This README file provides detailed setup instructions, information about the API endpoints, implementation details, and instructions for testing the project. It serves as a helpful guide for users, developers, and contributors to understand and use the project effectively.
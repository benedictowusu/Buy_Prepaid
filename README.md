# Customer Queue Management System

A Django-based web application to manage a customer queue for buying products. This project allows adding new customers, viewing the queue, and serving (removing) customers from the queue.

## Features

- **Add Customer**: Form to add new customers to the queue.
- **View Queue**: Displays a list of customers in the queue with details like name, meter number, and amount to buy.
- **Serve Customer**: Remove a customer from the queue and update the view to show the next customer.

## Installation

### Prerequisites

- Python 3.x
- Django 4.x
- (Optional) Virtual Environment

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/benedictowusu/Buy_Prepaid.git
   cd Buy_Prepaid
## Usage

### Adding a Customer

1. Navigate to the main page.
2. Fill out the customer form and submit to add a customer to the queue.

### Viewing the Queue

1. Navigate to the queue view page to see the list of customers.
2. The list shows the name, meter number, and amount to buy for each customer.

### Serving a Customer

1. On the queue view page, click the "Serve" button next to the customer's details.
2. The customer will be removed from the queue, and the view will update to show the next customer.

## URL Patterns

- `/` - Home page (Add Customer)
- `/view_queue/` - View Queue
- `/serve_buyer/<int:customer_id>/` - Serve Customer (Remove from queue)

## Contributing

Feel free to fork the repository and submit pull requests. If you find any issues or have suggestions, please open an issue on [GitHub Issues](https://github.com/benedictowusu/Buy_Prepaid/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

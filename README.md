# FIFO Calculation API and Stock Split API

This project is a Django-based API that provides functionality for FIFO (First-In-First-Out) calculation and stock split operations. The API allows users to perform FIFO calculations for stock valuation and handle stock split events.

## Features

The project offers the following main features:

1. FIFO Calculation API: This API endpoint allows users to calculate the valuation of stocks based on the FIFO method. It accepts the quantity and purchase price of each stock trade and returns the calculated valuation.

2. Stock Split API: This API endpoint enables users to process stock split events. It accepts the pre-split quantity and ratio and adjusts the quantity for each shareholder based on the split. The API returns the updated quantity of shares after the split.

3. GET APIs: The project also includes GET APIs to retrieve data related to FIFO calculations and stock splits. Users can retrieve information such as transaction statements, holding statements, and profit and loss reports for their stock portfolios.

## API Endpoints

The project provides the following API endpoints:

- `POST /fifo/fifoDataManage/`: Calculates the valuation of stocks using the FIFO method.
- `POST /fifo/stockSplitManage/`: Processes stock split events and updates the quantity of shares.
- `GET /fifo/fifoDataManage/`: Retrieves the fifo calculated data.
- `GET /fifo/stockSplitManage/`: Retrieves the holding statements for a stock portfolio.

## Prerequisites

Before running the project, ensure that you have the following dependencies installed:

- Python 

## Installation and Setup

To set up the project, follow these steps:

1. Clone the repository:

```
git clone https://github.com/CodeWithNeha/FIFO_STOCK.git
```

2. Navigate to the project directory:

```
cd your-project
```

3. Create and activate a virtual environment:

```
python -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate  # For Windows
```

4. Install the project dependencies:

```
pip install -r requirements.txt
```

5. Configure the project settings, including database settings

6. Run the database migrations:

```
python manage.py migrate
```

7. Start the development server:

```
python manage.py runserver
```

## Usage

Once the project is set up and the development server is running, you can make requests to the API endpoints using a tool like cURL, Postman, or any other HTTP client.

## Stock Split API

The Stock Split API allows users to handle stock split events. A stock split is a corporate action where the company divides its existing shares into multiple shares. This section describes how to use the Stock Split API:

### Request

- Method: POST
- Endpoint: `/fifo/stockSplitManage/`

#### Request Body

The request body should be a JSON object with the following fields:

- `user`: The username or identifier of the user.
- `total_amount_invested`: The total amount invested in the stock.
- `shares_pre_split`: The quantity of shares held before the stock split.
- `stock_split_ratio`: The ratio of the stock split. For example, if the ratio is 10:2, each shareholder will receive 10 shares for every 2 shares held previously.

#### Example

```json
{
  "user": "helo",
  "total_amount_invested": "8000",
  "shares_pre_split": 100,
  "stock_split_ratio": "10:2"
}
```


#### GET API OF STOCK SPLIT CAL

- Method: POST
- Endpoint: `/fifo/stockSplitManage/?user={user}`

#### Response

```json
{
  "data": {
    "id": 2,
    "user": "heena",
    "shares_pre_split": 100,
    "stock_split_ratio": "10:2",
    "shares_post_split": 500,
    "total_amount_invested": 8000.0,
    "avg_buy_price_post_split": 16.0,
    "updated_at": "2023-05-24T00:57:51.597172Z",
    "created_at": "2023-05-24T00:57:51.597172Z"
  },
  "message": "Data fetched successfully."
}
```

#### FIFO Calculation API

The FIFO Calculation API allows users to calculate the valuation of stocks using the FIFO method. This section describes how to use the FIFO Calculation API:

#### Request
Method: POST
Endpoint: `/fifo/fifoDataManage/`
#### Request Body
The request body should be a JSON object with the following fields:

-`days_data`: An array of objects representing each stock trade. Each object should have the following fields:
-`date`: The date of the trade.
-`company_name`: The name of the company.
-`trade_type`: The type of trade (BUY or SELL).
-`qty`: The quantity of shares traded.
-`buy_price`: The purchase price of the shares.
-`user`: The username or identifier of the user.

```json
{
  "days_data": [
    {"date": "3/8/2019", "company_name": "Apollo", "trade_type": "BUY", "qty": "10.00", "buy_price": "1389.55"},
    {"date": "6/24/2019", "company_name": "Apollo", "trade_type": "BUY", "qty": "3.00", "buy_price": "1531.58"},
    {"date": "9/27/2019", "company_name": "Apollo", "trade_type": "BUY", "qty": "13.00", "buy_price": "1376.20"},
    {"date": "10/22/2019", "company_name": "Apollo", "trade_type": "BUY", "qty": "10.00", "buy_price": "1394.12"},
    {"date": "10/23/2019", "company_name": "Apollo", "trade_type": "BUY", "qty": "10.00", "buy_price": "1383.49"},
    {"date": "1/3/2020", "company_name": "Apollo", "trade_type": "BUY", "qty": "4.00", "buy_price": "1903.69"},
    {"date": "6/22/2020", "company_name": "Apollo", "trade_type": "BUY", "qty": "22.00", "buy_price": "1600.04"},
    {"date": "7/14/2020", "company_name": "Apollo", "trade_type": "SELL", "qty": "37.00", "buy_price": "1702.58"},
    {"date": "7/20/2020", "company_name": "Apollo", "trade_type": "BUY", "qty": "22.00", "buy_price": "1813.93"},
    {"date": "7/27/2020", "company_name": "Apollo", "trade_type": "BUY", "qty": "7.00", "buy_price": "1907.71"},
    {"date": "9/8/2020", "company_name": "Apollo", "trade_type": "SELL", "qty": "32.00", "buy_price": "2472.56"}
  ],
  "user": "shiekh"
}
```

#### GET API OF FIFO CAL

- Method: POST
- Endpoint: `/fifo/fifoDataManage/?user={user}`

#### Response

```json
{
  "data": {
    "fifo_cal": [
      {
        "id": 66,
        "user": "shiekh",
        "date": "2019-03-08",
        "company_name": "Apollo",
        "trade_type": "BUY",
        "quantity": 10.0,
        "buy_price": 1389.55,
        "amount": 13895.5,
        "cummulative_cal": -59.0,
        "lot_pending_qty": null,
        "lot_value": null,
        "updated_at": "2023-05-24T01:06:26.781573Z",
        "created_at": "2023-05-24T01:06:26.781573Z"
      },
      {
        "id": 67,
        "user": "shiekh",
        "date": "2019-06-24",
        "company_name": "Apollo",
        "trade_type": "BUY",
        "quantity": 3.0,
        "buy_price": 1531.58,
        "amount": 4594.74,
        "cummulative_cal": -56.0,
        "lot_pending_qty": null,
        "lot_value": null,
        "updated_at": "2023-05-24T01:06:26.787470Z",
        "created_at": "2023-05-24T01:06:26.787470Z"
      },
      {
        "id": 68,
        "user": "shiekh",
        "date": "2019-09-27",
        "company_name": "Apollo",
        "trade_type": "BUY",
        "quantity": 13.0,
        "buy_price": 1376.2,
        "amount": 17890.600000000002,
        "cummulative_cal": -43.0,
        "lot_pending_qty": null,
        "lot_value": null,
        "updated_at": "2023-05-24T01:06:26.788461Z",
        "created_at": "2023-05-24T01:06:26.788461Z"
      },
      {
        "id": 69,
        "user": "shiekh",
        "date": "2019-10-22",
        "company_name": "Apollo",
        "trade_type": "BUY",
        "quantity": 10.0,
        "buy_price": 1394.12,
        "amount": 13941.199999999999,
        "cummulative_cal": -33.0,
        "lot_pending_qty": null,
        "lot_value": null,
        "updated_at": "2023-05-24T01:06:26.789459Z",
        "created_at": "2023-05-24T01:06:26.789459Z"
      },
      {
        "id": 70,
        "user": "shiekh",
        "date": "2019-10-23",
        "company_name": "Apollo",
        "trade_type": "BUY",
        "quantity": 10.0,
        "buy_price": 1383.49,
        "amount": 13834.9,
        "cummulative_cal": -23.0,
        "lot_pending_qty": null,
        "lot_value": null,
        "updated_at": "2023-05-24T01:06:26.790427Z",
        "created_at": "2023-05-24T01:06:26.790427Z"
      },
      {
        "id": 71,
        "user": "shiekh",
        "date": "2020-01-03",
        "company_name": "Apollo",
        "trade_type": "BUY",
        "quantity": 4.0,
        "buy_price": 1903.69,
        "amount": 7614.76,
        "cummulative_cal": -19.0,
        "lot_pending_qty": null,
        "lot_value": null,
        "updated_at": "2023-05-24T01:06:26.790427Z",
        "created_at": "2023-05-24T01:06:26.790427Z"
      },
      {
        "id": 72,
        "user": "shiekh",
        "date": "2020-06-22",
        "company_name": "Apollo",
        "trade_type": "BUY",
        "quantity": 22.0,
        "buy_price": 1600.04,
        "amount": 35200.88,
        "cummulative_cal": 3.0,
        "lot_pending_qty": 3.0,
        "lot_value": 4800.12,
        "updated_at": "2023-05-24T01:06:26.791453Z",
        "created_at": "2023-05-24T01:06:26.791453Z"
      },
      {
        "id": 73,
        "user": "shiekh",
        "date": "2020-07-14",
        "company_name": "Apollo",
        "trade_type": "SELL",
        "quantity": 37.0,
        "buy_price": 1702.58,
        "amount": 62995.46,
        "cummulative_cal": null,
        "lot_pending_qty": null,
        "lot_value": null,
        "updated_at": "2023-05-24T01:06:26.792422Z",
        "created_at": "2023-05-24T01:06:26.792422Z"
      },
      {
        "id": 74,
        "user": "shiekh",
        "date": "2020-07-20",
        "company_name": "Apollo",
        "trade_type": "BUY",
        "quantity": 22.0,
        "buy_price": 1813.93,
        "amount": 39906.46,
        "cummulative_cal": 22.0,
        "lot_pending_qty": 22.0,
        "lot_value": 39906.46,
        "updated_at": "2023-05-24T01:06:26.793419Z",
        "created_at": "2023-05-24T01:06:26.793419Z"
      },
      {
        "id": 75,
        "user": "shiekh",
        "date": "2020-07-27",
        "company_name": "Apollo",
        "trade_type": "BUY",
        "quantity": 7.0,
        "buy_price": 1907.71,
        "amount": 13353.970000000001,
        "cummulative_cal": 29.0,
        "lot_pending_qty": 7.0,
        "lot_value": 13353.970000000001,
        "updated_at": "2023-05-24T01:06:26.794416Z",
        "created_at": "2023-05-24T01:06:26.794416Z"
      },
      {
        "id": 76,
        "user": "shiekh",
        "date": "2020-09-08",
        "company_name": "Apollo",
        "trade_type": "SELL",
        "quantity": 32.0,
        "buy_price": 2472.56,
        "amount": 79121.92,
        "cummulative_cal": null,
        "lot_pending_qty": null,
        "lot_value": null,
        "updated_at": "2023-05-24T01:06:26.796429Z",
        "created_at": "2023-05-24T01:06:26.796429Z"
      }
    ],
    "avg_buying_price_cal": {
      "id": 6,
      "user": "shiekh",
      "total_buy_qty": 101.0,
      "total_sell_qty": 69.0,
      "closing_qty": 32.0,
      "closing_value": 58060.55,
      "avg_buying_price": 1814.3921875,
      "updated_at": "2023-05-24T01:06:26.797418Z",
      "created_at": "2023-05-24T01:06:26.797418Z"
    }
  },
  "message": "Data fetched successfully."
}
```

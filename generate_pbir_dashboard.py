import os
import json

REPORT_DIR = r"c:\Users\pedda\OneDrive\Documents\E-Commerce-Sales-Analytics\E-Commerce-Sales-Analytics-Executive.Report"
PAGE_ID = "dc5ffb9e39267074c399"
PAGES_DIR = os.path.join(REPORT_DIR, "definition", "pages", PAGE_ID)
VISUALS_DIR = os.path.join(PAGES_DIR, "visuals")

SCHEMA_URL = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.14.0/schema.json"

def col_ref(entity, prop):
    return {
        "Column": {
            "Expression": {
                "SourceRef": {
                    "Entity": entity
                }
            },
            "Property": prop
        }
    }

def meas_ref(entity, prop):
    return {
        "Measure": {
            "Expression": {
                "SourceRef": {
                    "Entity": entity
                }
            },
            "Property": prop
        }
    }

def create_title(text):
    return {
        "title": [
            {
                "properties": {
                    "show": {
                        "expr": {
                            "Literal": {
                                "Value": "true"
                            }
                        }
                    },
                    "text": {
                        "expr": {
                            "Literal": {
                                "Value": f"'{text}'"
                            }
                        }
                    }
                }
            }
        ]
    }

def make_card(name, tab_order, x, y, width, height, title_text, meas_name):
    return {
        "$schema": SCHEMA_URL,
        "name": name,
        "position": {
            "x": x,
            "y": y,
            "z": tab_order,
            "width": width,
            "height": height,
            "tabOrder": tab_order
        },
        "visual": {
            "visualType": "card",
            "query": {
                "queryState": {
                    "Values": {
                        "projections": [
                            {
                                "field": meas_ref("cleaned_customers", meas_name),
                                "queryRef": f"cleaned_customers.{meas_name}"
                            }
                        ]
                    }
                }
            },
            "visualContainerObjects": create_title(title_text)
        }
    }

def make_slicer(name, tab_order, x, y, width, height, title_text, entity, col_name):
    return {
        "$schema": SCHEMA_URL,
        "name": name,
        "position": {
            "x": x,
            "y": y,
            "z": tab_order,
            "width": width,
            "height": height,
            "tabOrder": tab_order
        },
        "visual": {
            "visualType": "slicer",
            "query": {
                "queryState": {
                    "Values": {
                        "projections": [
                            {
                                "field": col_ref(entity, col_name),
                                "queryRef": f"{entity}.{col_name}"
                            }
                        ]
                    }
                }
            },
            "visualContainerObjects": create_title(title_text)
        }
    }

def make_line_chart(name, tab_order, x, y, width, height, title_text):
    return {
        "$schema": SCHEMA_URL,
        "name": name,
        "position": {
            "x": x,
            "y": y,
            "z": tab_order,
            "width": width,
            "height": height,
            "tabOrder": tab_order
        },
        "visual": {
            "visualType": "lineChart",
            "query": {
                "queryState": {
                    "Category": {
                        "projections": [
                            {
                                "field": col_ref("cleaned_orders", "OrderDate"),
                                "queryRef": "cleaned_orders.OrderDate"
                            }
                        ]
                    },
                    "Y": {
                        "projections": [
                            {
                                "field": meas_ref("cleaned_customers", "Total Revenue"),
                                "queryRef": "cleaned_customers.Total Revenue"
                            }
                        ]
                    }
                },
                "sortDefinition": {
                    "sort": [
                        {
                            "field": col_ref("cleaned_orders", "OrderDate"),
                            "direction": "Ascending"
                        }
                    ],
                    "isDefaultSort": False
                }
            },
            "visualContainerObjects": create_title(title_text)
        }
    }

def make_clustered_column(name, tab_order, x, y, width, height, title_text):
    return {
        "$schema": SCHEMA_URL,
        "name": name,
        "position": {
            "x": x,
            "y": y,
            "z": tab_order,
            "width": width,
            "height": height,
            "tabOrder": tab_order
        },
        "visual": {
            "visualType": "clusteredColumnChart",
            "query": {
                "queryState": {
                    "Category": {
                        "projections": [
                            {
                                "field": col_ref("cleaned_regions", "RegionName"),
                                "queryRef": "cleaned_regions.RegionName"
                            }
                        ]
                    },
                    "Y": {
                        "projections": [
                            {
                                "field": meas_ref("cleaned_customers", "Total Revenue"),
                                "queryRef": "cleaned_customers.Total Revenue"
                            },
                            {
                                "field": meas_ref("cleaned_customers", "Total Profit"),
                                "queryRef": "cleaned_customers.Total Profit"
                            }
                        ]
                    }
                },
                "sortDefinition": {
                    "sort": [
                        {
                            "field": meas_ref("cleaned_customers", "Total Revenue"),
                            "direction": "Descending"
                        }
                    ],
                    "isDefaultSort": False
                }
            },
            "visualContainerObjects": create_title(title_text)
        }
    }

def make_clustered_bar(name, tab_order, x, y, width, height, title_text):
    return {
        "$schema": SCHEMA_URL,
        "name": name,
        "position": {
            "x": x,
            "y": y,
            "z": tab_order,
            "width": width,
            "height": height,
            "tabOrder": tab_order
        },
        "visual": {
            "visualType": "clusteredBarChart",
            "query": {
                "queryState": {
                    "Category": {
                        "projections": [
                            {
                                "field": col_ref("cleaned_products", "Category"),
                                "queryRef": "cleaned_products.Category"
                            }
                        ]
                    },
                    "Y": {
                        "projections": [
                            {
                                "field": meas_ref("cleaned_customers", "Total Revenue"),
                                "queryRef": "cleaned_customers.Total Revenue"
                            }
                        ]
                    }
                },
                "sortDefinition": {
                    "sort": [
                        {
                            "field": meas_ref("cleaned_customers", "Total Revenue"),
                            "direction": "Descending"
                        }
                    ],
                    "isDefaultSort": False
                }
            },
            "visualContainerObjects": create_title(title_text)
        }
    }

def make_donut_chart(name, tab_order, x, y, width, height, title_text, cat_entity, cat_col, val_entity, val_meas):
    return {
        "$schema": SCHEMA_URL,
        "name": name,
        "position": {
            "x": x,
            "y": y,
            "z": tab_order,
            "width": width,
            "height": height,
            "tabOrder": tab_order
        },
        "visual": {
            "visualType": "donutChart",
            "query": {
                "queryState": {
                    "Category": {
                        "projections": [
                            {
                                "field": col_ref(cat_entity, cat_col),
                                "queryRef": f"{cat_entity}.{cat_col}"
                            }
                        ]
                    },
                    "Y": {
                        "projections": [
                            {
                                "field": meas_ref(val_entity, val_meas),
                                "queryRef": f"{val_entity}.{val_meas}"
                            }
                        ]
                    }
                },
                "sortDefinition": {
                    "sort": [
                        {
                            "field": meas_ref(val_entity, val_meas),
                            "direction": "Descending"
                        }
                    ],
                    "isDefaultSort": False
                }
            },
            "visualContainerObjects": create_title(title_text)
        }
    }

def main():
    os.makedirs(VISUALS_DIR, exist_ok=True)
    
    # 1. Update page.json displayName to Executive Overview
    page_json_path = os.path.join(PAGES_DIR, "page.json")
    page_data = {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.1.0/schema.json",
        "name": PAGE_ID,
        "displayName": "Executive Overview",
        "displayOption": "FitToPage",
        "height": 1080,
        "width": 1920
    }
    with open(page_json_path, "w", encoding="utf-8") as f:
        json.dump(page_data, f, indent=2)
    print("Updated page.json with displayName 'Executive Overview'")

    visuals = [
        # Slicers (Row 1: y=20, h=95)
        make_slicer("slicer_order_date", 1000, 30, 20, 440, 95, "Order Date Range", "cleaned_orders", "OrderDate"),
        make_slicer("slicer_region", 2000, 490, 20, 440, 95, "Region", "cleaned_regions", "RegionName"),
        make_slicer("slicer_category", 3000, 950, 20, 450, 95, "Product Category", "cleaned_products", "Category"),
        make_slicer("slicer_payment_method", 4000, 1420, 20, 470, 95, "Payment Method", "cleaned_orders", "PaymentMethod"),
        
        # KPI Cards (Row 2: y=135, h=140)
        make_card("kpi_total_revenue", 5000, 30, 135, 440, 140, "Total Revenue", "Total Revenue"),
        make_card("kpi_total_profit", 6000, 490, 135, 440, 140, "Total Profit", "Total Profit"),
        make_card("kpi_total_orders", 7000, 950, 135, 450, 140, "Total Orders", "Total Orders"),
        make_card("kpi_avg_order_value", 8000, 1420, 135, 470, 140, "Average Order Value", "Average Order Value"),
        
        # Primary Trends (Row 3: y=295, h=370)
        make_line_chart("chart_monthly_revenue", 9000, 30, 295, 1000, 370, "Monthly Revenue Trend"),
        make_clustered_column("chart_regional_performance", 10000, 1050, 295, 840, 370, "Revenue vs Profit by Region"),
        
        # Category & Breakdowns (Row 4: y=685, h=370)
        make_clustered_bar("chart_category_revenue", 11000, 30, 685, 610, 370, "Revenue by Product Category"),
        make_donut_chart("chart_order_status", 12000, 660, 685, 580, 370, "Orders by Order Status", "cleaned_orders", "OrderStatus", "cleaned_customers", "Total Orders"),
        make_donut_chart("chart_payment_revenue", 13000, 1260, 685, 630, 370, "Revenue by Payment Method", "cleaned_orders", "PaymentMethod", "cleaned_customers", "Total Revenue"),
    ]
    
    for v in visuals:
        v_name = v["name"]
        v_dir = os.path.join(VISUALS_DIR, v_name)
        os.makedirs(v_dir, exist_ok=True)
        v_path = os.path.join(v_dir, "visual.json")
        with open(v_path, "w", encoding="utf-8") as f:
            json.dump(v, f, indent=2)
        print(f"Generated: {v_name}/visual.json")

    print(f"\nAll {len(visuals)} visuals generated successfully!")

if __name__ == "__main__":
    main()

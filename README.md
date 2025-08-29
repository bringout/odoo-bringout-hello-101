# odoo-bringout-hello-101

Hello 101

## Overview

This is a custom Odoo 16 module that provides:

- **Interactive Menu**: Custom menu item "Hello 101"
- **Hello Message**: Personalized greeting using OWL JavaScript component
- **Modern UI**: Built with Odoo's OWL framework for reactive interfaces
- **RESTful API**: HTTP endpoints for dynamic content loading

## Features

### 🎯 Main Features
- Custom menu integration in Odoo backend
- Interactive hello message with user personalization
- Modern JavaScript component using OWL framework
- Responsive design for mobile and desktop
- Real-time message refresh functionality

### 🛠️ Technical Features
- **OWL Component**: Modern JavaScript framework for Odoo
- **HTTP Controllers**: RESTful API endpoints
- **Asset Management**: Proper CSS/JS asset loading
- **Security**: User authentication and access control
- **Responsive Design**: Mobile-friendly interface

## Installation

### Prerequisites
- Odoo 16.0
- Python 3.8+

### Install from PyPI
```bash
pip install odoo-bringout-hello-101
# or
uv pip install odoo-bringout-hello-101
```

### Install from Source
```bash
git clone <repository-url>
cd odoo-bringout-hello-101
pip install -e .
```

### Odoo Configuration
Add the addon to your Odoo addons path and install it through the Apps interface.

## Usage

1. **Install the Module**: Go to Apps → Search for "Hello 101" → Install
2. **Access the Feature**: Click on "Hello 101" in the main menu
3. **Interact**: The page will load with a personalized greeting
4. **Refresh**: Click "Refresh Message" to reload the greeting

### API Endpoints

The module provides several HTTP endpoints:

- `GET /hello_101/hello` - Returns personalized hello message (JSON)
- `GET /hello_101/dashboard` - Renders the main dashboard page

## Development

### Project Structure
```
odoo-bringout-hello-101/
├── hello_101/                 # Main addon directory
│   ├── __manifest__.py               # Addon manifest
│   ├── controllers/                  # HTTP controllers
│   ├── models/                       # Data models (if any)
│   ├── views/                        # XML views and menus
│   ├── data/                         # Demo/seed data
│   ├── security/                     # Access control
│   └── static/                       # Frontend assets
│       └── src/
│           ├── js/                   # JavaScript/OWL components
│           ├── css/                  # Stylesheets
│           └── xml/                  # OWL templates
├── setup.py                          # Python package setup
└── README.md                         # This file
```

### Key Components

#### OWL JavaScript Component (`hello_component.js`)
```javascript
class HelloComponent extends Component {
    // Reactive state management
    // HTTP API integration
    // Event handling
}
```

#### Controller (`controllers/main.py`)
```python
@http.route('/hello_101/hello', type='json', auth='user')
def get_hello_message(self, **kwargs):
    # Returns personalized greeting
```

### Customization

You can customize the module by:

1. **Modifying Messages**: Edit the controller to change greeting logic
2. **Styling**: Update CSS files in `static/src/css/`
3. **Templates**: Modify OWL templates in `static/src/xml/`
4. **Adding Features**: Extend with new models, views, or controllers

## Configuration

### Environment Variables
- `ODOO_ADDONS_PATH`: Include the module path
- Standard Odoo configuration applies

### Settings
Access module settings through:
- Settings → Technical → Parameters → System Parameters
- Search for parameters starting with `hello_101.`

## Troubleshooting

### Common Issues

**Module not appearing in Apps**
- Verify addons path configuration
- Check __manifest__.py syntax
- Restart Odoo server with `--update=all`

**JavaScript errors**
- Check browser console for OWL-related errors
- Verify asset paths in __manifest__.py
- Clear browser cache

**Permission errors**
- Check security/ir.model.access.csv
- Verify user has proper access rights

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes with tests
4. Submit a pull request

## License

This project is licensed under the AGPL-3 License.

## Support

For support and questions:
- **Website**: https://www.bring.out.ba
- **Documentation**: See inline code comments and Odoo documentation
- **Issues**: Report bugs through the project issue tracker

---

**Author**: Bringout  
**Version**: 16.0.1.0.0  
**Odoo Version**: 16.0+

## Documentation

- Overview: doc/OVERVIEW.md
- Architecture: doc/ARCHITECTURE.md
- Models: doc/MODELS.md
- Controllers: doc/CONTROLLERS.md
- Wizards: doc/WIZARDS.md
- Install: doc/INSTALL.md
- Usage: doc/USAGE.md
- Configuration: doc/CONFIGURATION.md
- Dependencies: doc/DEPENDENCIES.md
- Troubleshooting: doc/TROUBLESHOOTING.md
- FAQ: doc/FAQ.md

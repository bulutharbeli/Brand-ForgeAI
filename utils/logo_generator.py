import random
import json

class LogoConceptGenerator:
    """Generate logo design concepts and suggestions"""
    
    def __init__(self):
        self.design_styles = {
            'minimalist': {
                'characteristics': ['clean lines', 'simple shapes', 'negative space', 'typography-focused'],
                'best_for': ['technology', 'consulting', 'finance'],
                'examples': ['Nike', 'Apple', 'Airbnb']
            },
            'modern': {
                'characteristics': ['geometric shapes', 'gradients', 'bold typography', 'asymmetrical'],
                'best_for': ['technology', 'startups', 'digital services'],
                'examples': ['Spotify', 'Slack', 'Stripe']
            },
            'classic': {
                'characteristics': ['serif fonts', 'crests', 'symmetrical', 'traditional elements'],
                'best_for': ['law firms', 'universities', 'luxury brands'],
                'examples': ['Harvard', 'Rolex', 'CNN']
            },
            'playful': {
                'characteristics': ['bright colors', 'rounded shapes', 'fun typography', 'mascots'],
                'best_for': ['children products', 'entertainment', 'food & beverage'],
                'examples': ['Disney', 'Lego', 'McDonalds']
            },
            'abstract': {
                'characteristics': ['symbolic shapes', 'unique forms', 'memorable marks', 'versatile'],
                'best_for': ['technology', 'consulting', 'arts'],
                'examples': ['Pepsi', 'Adidas', 'Mastercard']
            },
            'vintage': {
                'characteristics': ['retro fonts', 'textures', 'ornamental details', 'aged effects'],
                'best_for': ['craft breweries', 'barbershops', 'restaurants'],
                'examples': ['Levi\'s', 'Coca-Cola', 'Harley Davidson']
            },
            'hand_drawn': {
                'characteristics': ['sketched elements', 'organic lines', 'personal touch', 'artistic'],
                'best_for': ['artisanal products', 'cafes', 'creative agencies'],
                'examples': ['Ben & Jerry\'s', 'Etsy', 'Innocent']
            }
        }
        
        self.industry_symbols = {
            'technology': ['circuit patterns', 'digital nodes', 'abstract data flows', 'geometric tech shapes'],
            'healthcare': ['cross symbols', 'heart shapes', 'DNA helix', 'medical crosses'],
            'finance': ['arrows', 'graphs', 'shield symbols', 'growth charts'],
            'education': ['books', 'graduation caps', 'light bulbs', 'pencils'],
            'retail': ['shopping bags', 'hangers', 'price tags', 'store fronts'],
            'food': ['utensils', 'plates', 'ingredient silhouettes', 'steam lines'],
            'travel': ['airplanes', 'compasses', 'globes', 'luggage'],
            'fitness': ['dumbbells', 'running figures', 'heart rates', 'mountains']
        }
    
    def generate_concepts(self, brand_name, industry, style='minimalist'):
        """Generate logo design concepts"""
        concepts = []
        
        # Get style guidelines
        style_info = self.design_styles.get(style.lower(), self.design_styles['modern'])
        
        # Get industry symbols
        symbols = self.industry_symbols.get(industry.lower(), ['abstract shape', 'geometric pattern'])
        
        # Generate 5 different concepts
        concept_types = ['lettermark', 'wordmark', 'pictorial', 'abstract', 'mascot']
        
        for i, concept_type in enumerate(concept_types):
            concept = {
                'id': i + 1,
                'type': concept_type,
                'title': f"{concept_type.title()} Logo Concept",
                'description': self._generate_concept_description(concept_type, brand_name, industry, style),
                'design_elements': self._get_design_elements(concept_type, symbols, style_info),
                'color_suggestions': self._suggest_colors(industry, style),
                'typography': self._suggest_typography(style),
                'layout': self._suggest_layout(concept_type),
                'style_notes': style_info['characteristics'],
                'best_for': style_info['best_for'],
                'similar_to': random.sample(style_info['examples'], min(2, len(style_info['examples']))),
                'implementation_tips': self._get_implementation_tips(concept_type)
            }
            concepts.append(concept)
        
        return concepts
    
    def _generate_concept_description(self, concept_type, brand_name, industry, style):
        """Generate a description for the logo concept"""
        descriptions = {
            'lettermark': f"A {style} lettermark using the initials from '{brand_name}'. Focuses on typography and negative space to create a memorable mark.",
            'wordmark': f"A {style} wordmark featuring '{brand_name}' in a custom typeface. The text itself becomes the logo with carefully crafted letterforms.",
            'pictorial': f"A {style} pictorial mark combining '{brand_name}' with a recognizable symbol from the {industry} industry. Creates strong visual association.",
            'abstract': f"An abstract {style} symbol for '{brand_name}' that doesn't directly represent anything but creates a unique, memorable visual identity.",
            'mascot': f"A {style} mascot or character that embodies '{brand_name}' and appeals to the {industry} audience. Great for building brand personality."
        }
        return descriptions.get(concept_type, f"A {style} logo design for {brand_name}")
    
    def _get_design_elements(self, concept_type, symbols, style_info):
        """Get design elements for the concept"""
        elements = []
        
        if concept_type == 'lettermark':
            elements = [
                'Custom letterforms',
                'Negative space usage',
                'Geometric construction',
                'Balanced proportions'
            ]
        elif concept_type == 'wordmark':
            elements = [
                'Custom typeface design',
                'Letter spacing optimization',
                'Unique letter modifications',
                'Clear readability'
            ]
        elif concept_type == 'pictorial':
            elements = [
                random.choice(symbols),
                'Clean line work',
                'Scalable vector design',
                'Iconic simplification'
            ]
        elif concept_type == 'abstract':
            elements = [
                'Unique geometric shape',
                'Symbolic meaning',
                'Versatile application',
                'Memorable silhouette'
            ]
        elif concept_type == 'mascot':
            elements = [
                'Character design',
                'Friendly expression',
                'Brand personality',
                'Versatile poses'
            ]
        
        # Add style-specific elements
        elements.extend(style_info['characteristics'][:2])
        
        return elements
    
    def _suggest_colors(self, industry, style):
        """Suggest color schemes for the logo"""
        color_suggestions = {
            'technology': ['#2563EB', '#7C3AED', '#0891B2'],
            'healthcare': ['#0D9488', '#059669', '#2563EB'],
            'finance': ['#1E40AF', '#059669', '#7C3AED'],
            'education': ['#7C3AED', '#2563EB', '#0891B2'],
            'retail': ['#DB2777', '#DC2626', '#F59E0B'],
            'food': ['#DC2626', '#F59E0B', '#D97706'],
            'travel': ['#0891B2', '#2563EB', '#059669'],
            'fitness': ['#DC2626', '#059669', '#F59E0B']
        }
        
        base_colors = color_suggestions.get(industry.lower(), ['#000000', '#3B82F6', '#10B981'])
        
        return {
            'primary': base_colors[0],
            'secondary': base_colors[1] if len(base_colors) > 1 else '#6B7280',
            'accent': base_colors[2] if len(base_colors) > 2 else '#F59E0B',
            'note': f"Use these colors in a {style} manner with appropriate contrast ratios"
        }
    
    def _suggest_typography(self, style):
        """Suggest typography for the logo"""
        typography_suggestions = {
            'minimalist': {
                'fonts': ['Helvetica Neue', 'Arial', 'Futura', 'Gotham'],
                'characteristics': ['clean', 'sans-serif', 'geometric', 'simple']
            },
            'modern': {
                'fonts': ['Montserrat', 'Roboto', 'Open Sans', 'Proxima Nova'],
                'characteristics': ['contemporary', 'versatile', 'web-friendly', 'clean']
            },
            'classic': {
                'fonts': ['Times New Roman', 'Georgia', 'Garamond', 'Baskerville'],
                'characteristics': ['serif', 'traditional', 'elegant', 'authoritative']
            },
            'playful': {
                'fonts': ['Comic Sans MS', 'Fredoka One', 'Nunito', 'Quicksand'],
                'characteristics': ['rounded', 'friendly', 'fun', 'approachable']
            },
            'abstract': {
                'fonts': ['Montserrat', 'Raleway', 'Lato', 'Poppins'],
                'characteristics': ['modern', 'clean', 'versatile', 'balanced']
            },
            'vintage': {
                'fonts': ['Playfair Display', 'Crimson Text', 'Lobster', 'Pacifico'],
                'characteristics': ['retro', 'textured', 'ornamental', 'classic']
            },
            'hand_drawn': {
                'fonts': ['Brush Script', 'Handlee', 'Caveat', 'Dancing Script'],
                'characteristics': ['organic', 'artistic', 'personal', 'sketched']
            }
        }
        
        suggestion = typography_suggestions.get(style.lower(), typography_suggestions['modern'])
        
        return {
            'recommended_fonts': suggestion['fonts'],
            'characteristics': suggestion['characteristics'],
            'note': 'Consider customizing the typeface to make it unique to the brand'
        }
    
    def _suggest_layout(self, concept_type):
        """Suggest layout options for the logo"""
        layouts = {
            'lettermark': [
                'Centered letterform',
                'Stacked initials',
                'Interlocking letters',
                'Negative space integration'
            ],
            'wordmark': [
                'Horizontal layout',
                'Stacked text',
                'Custom letter spacing',
                'Integrated symbol'
            ],
            'pictorial': [
                'Icon above text',
                'Icon left of text',
                'Icon right of text',
                'Icon integrated with text'
            ],
            'abstract': [
                'Symbol centered',
                'Symbol with text below',
                'Symbol with text beside',
                'Standalone symbol'
            ],
            'mascot': [
                'Character centered',
                'Character with text below',
                'Character holding text',
                'Character as container'
            ]
        }
        
        return layouts.get(concept_type, ['Horizontal layout', 'Vertical layout', 'Icon with text'])
    
    def _get_implementation_tips(self, concept_type):
        """Get implementation tips for the logo concept"""
        tips = {
            'lettermark': [
                'Ensure the logo works in monochrome',
                'Test at small sizes (favicon, social media)',
                'Create clear space guidelines',
                'Develop a grid system for consistency'
            ],
            'wordmark': [
                'Kern the letters carefully',
                'Ensure readability at all sizes',
                'Consider custom letter modifications',
                'Create web and print versions'
            ],
            'pictorial': [
                'Keep the symbol simple and recognizable',
                'Ensure it works without color',
                'Make it scalable from favicon to billboard',
                'Test recognition at small sizes'
            ],
            'abstract': [
                'Make it unique and ownable',
                'Ensure it has symbolic meaning',
                'Test for cultural sensitivity',
                'Create guidelines for correct usage'
            ],
            'mascot': [
                'Create multiple poses/expressions',
                'Ensure the character is likable',
                'Develop character personality guidelines',
                'Make it adaptable for different contexts'
            ]
        }
        
        return tips.get(concept_type, ['Keep it simple', 'Ensure scalability', 'Test in context'])

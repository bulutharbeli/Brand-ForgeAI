import random
import math

class ColorPaletteGenerator:
    """Generate brand color palettes based on color theory and psychology"""
    
    def __init__(self):
        # Color psychology by industry
        self.industry_colors = {
            'technology': {
                'primary': ['#2563EB', '#7C3AED', '#0891B2', '#059669'],
                'mood': 'innovative',
                'associations': ['trust', 'innovation', 'reliability']
            },
            'healthcare': {
                'primary': ['#0D9488', '#059669', '#2563EB', '#7C3AED'],
                'mood': 'healing',
                'associations': ['health', 'trust', 'calm']
            },
            'finance': {
                'primary': ['#1E40AF', '#059669', '#7C3AED', '#065F46'],
                'mood': 'trustworthy',
                'associations': ['stability', 'growth', 'security']
            },
            'education': {
                'primary': ['#7C3AED', '#2563EB', '#0891B2', '#D97706'],
                'mood': 'inspiring',
                'associations': ['knowledge', 'growth', 'creativity']
            },
            'retail': {
                'primary': ['#DB2777', '#DC2626', '#F59E0B', '#7C3AED'],
                'mood': 'energetic',
                'associations': ['excitement', 'style', 'trend']
            },
            'food': {
                'primary': ['#DC2626', '#F59E0B', '#D97706', '#059669'],
                'mood': 'appetizing',
                'associations': ['appetite', 'freshness', 'taste']
            },
            'travel': {
                'primary': ['#0891B2', '#2563EB', '#059669', '#7C3AED'],
                'mood': 'adventurous',
                'associations': ['exploration', 'freedom', 'discovery']
            },
            'fitness': {
                'primary': ['#DC2626', '#059669', '#F59E0B', '#7C3AED'],
                'mood': 'energizing',
                'associations': ['energy', 'strength', 'vitality']
            }
        }
        
        # Mood-based color schemes
        self.mood_colors = {
            'professional': ['#1E3A8A', '#475569', '#64748B', '#94A3B8'],
            'playful': ['#EC4899', '#F59E0B', '#10B981', '#6366F1'],
            'luxury': ['#1C1917', '#57534E', '#A8A29E', '#D6D3D1'],
            'modern': ['#000000', '#3B82F6', '#10B981', '#8B5CF6'],
            'trustworthy': ['#1E40AF', '#3B82F6', '#60A5FA', '#93C5FD'],
            'energetic': ['#DC2626', '#F59E0B', '#10B981', '#6366F1'],
            'calming': ['#0D9488', '#06B6D4', '#3B82F6', '#8B5CF6'],
            'bold': ['#000000', '#DC2626', '#F59E0B', '#059669']
        }
    
    def generate_palette(self, industry, mood='professional', primary_color=None):
        """Generate a complete color palette"""
        palette = {
            'primary': '',
            'secondary': '',
            'accent': '',
            'neutral': '',
            'success': '',
            'warning': '',
            'error': '',
            'info': '',
            'hex_codes': [],
            'color_names': [],
            'usage_guidelines': {}
        }
        
        # Get base colors from industry or mood
        if primary_color:
            palette['primary'] = primary_color
            generated_colors = self._generate_from_primary(primary_color)
        else:
            if industry.lower() in self.industry_colors:
                base_colors = self.industry_colors[industry.lower()]['primary']
                palette['primary'] = random.choice(base_colors)
            else:
                base_colors = self.mood_colors.get(mood.lower(), self.mood_colors['professional'])
                palette['primary'] = random.choice(base_colors)
            
            generated_colors = self._generate_complementary_palette(palette['primary'])
        
        # Assign generated colors to palette roles
        palette['secondary'] = generated_colors.get('secondary', '#6B7280')
        palette['accent'] = generated_colors.get('accent', '#F59E0B')
        palette['neutral'] = generated_colors.get('neutral', '#F3F4F6')
        palette['success'] = generated_colors.get('success', '#10B981')
        palette['warning'] = generated_colors.get('warning', '#F59E0B')
        palette['error'] = generated_colors.get('error', '#EF4444')
        palette['info'] = generated_colors.get('info', '#3B82F6')
        
        # Generate hex codes list
        palette['hex_codes'] = [
            palette['primary'],
            palette['secondary'],
            palette['accent'],
            palette['neutral'],
            palette['success'],
            palette['warning'],
            palette['error'],
            palette['info']
        ]
        
        # Generate color names
        palette['color_names'] = [self._get_color_name(c) for c in palette['hex_codes']]
        
        # Usage guidelines
        palette['usage_guidelines'] = {
            'primary': 'Use for main branding, logos, and primary CTAs',
            'secondary': 'Use for subheadings, secondary buttons, and supporting elements',
            'accent': 'Use sparingly for highlights, links, and emphasis',
            'neutral': 'Use for backgrounds, borders, and text on dark backgrounds',
            'success': 'Use for success messages and positive indicators',
            'warning': 'Use for warning messages and caution indicators',
            'error': 'Use for error messages and critical alerts',
            'info': 'Use for informational messages and neutral alerts'
        }
        
        return palette
    
    def _generate_complementary_palette(self, primary_color):
        """Generate a complementary color palette from a primary color"""
        # Convert hex to RGB
        r, g, b = self._hex_to_rgb(primary_color)
        
        # Generate secondary (complementary)
        secondary = self._generate_complementary(r, g, b)
        
        # Generate accent (analogous or triadic)
        accent = self._generate_accent(r, g, b)
        
        # Generate neutral (tint of primary)
        neutral = self._generate_neutral(r, g, b)
        
        return {
            'secondary': secondary,
            'accent': accent,
            'neutral': neutral
        }
    
    def _generate_from_primary(self, primary_color):
        """Generate full palette from a user-provided primary color"""
        return self._generate_complementary_palette(primary_color)
    
    def _hex_to_rgb(self, hex_color):
        """Convert hex color to RGB"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def _rgb_to_hex(self, r, g, b):
        """Convert RGB to hex"""
        return '#{:02x}{:02x}{:02x}'.format(
            max(0, min(255, int(r))),
            max(0, min(255, int(g))),
            max(0, min(255, int(b)))
        )
    
    def _generate_complementary(self, r, g, b):
        """Generate complementary color"""
        # Simple complementary: invert the color
        comp_r = 255 - r
        comp_g = 255 - g
        comp_b = 255 - b
        
        # Adjust to make it more visually appealing
        avg = (r + g + b) / 3
        if avg > 127:
            # For light colors, darken the complement
            comp_r = int(comp_r * 0.7)
            comp_g = int(comp_g * 0.7)
            comp_b = int(comp_b * 0.7)
        else:
            # For dark colors, lighten the complement
            comp_r = int(comp_r + (255 - comp_r) * 0.3)
            comp_g = int(comp_g + (255 - comp_g) * 0.3)
            comp_b = int(comp_b + (255 - comp_b) * 0.3)
        
        return self._rgb_to_hex(comp_r, comp_g, comp_b)
    
    def _generate_accent(self, r, g, b):
        """Generate accent color (analogous or triadic)"""
        # Convert to HSL-like values
        h, s, l = self._rgb_to_hsl(r, g, b)
        
        # Shift hue by 30 degrees for analogous
        h = (h + 30) % 360
        
        # Adjust saturation and lightness
        s = min(100, s + 10)
        l = max(30, min(70, l))
        
        acc_r, acc_g, acc_b = self._hsl_to_rgb(h, s, l)
        return self._rgb_to_hex(acc_r, acc_g, acc_b)
    
    def _generate_neutral(self, r, g, b):
        """Generate neutral color (tint/shade of primary)"""
        # Create a light tint
        tint_r = int(r + (255 - r) * 0.9)
        tint_g = int(g + (255 - g) * 0.9)
        tint_b = int(b + (255 - b) * 0.9)
        
        return self._rgb_to_hex(tint_r, tint_g, tint_b)
    
    def _rgb_to_hsl(self, r, g, b):
        """Convert RGB to HSL (simplified)"""
        r, g, b = r/255, g/255, b/255
        max_c = max(r, g, b)
        min_c = min(r, g, b)
        l = (max_c + min_c) / 2
        
        if max_c == min_c:
            h = s = 0
        else:
            d = max_c - min_c
            s = d / (2 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)
            
            if max_c == r:
                h = (g - b) / d + (6 if g < b else 0)
            elif max_c == g:
                h = (b - r) / d + 2
            else:
                h = (r - g) / d + 4
            h /= 6
        
        return h * 360, s * 100, l * 100
    
    def _hsl_to_rgb(self, h, s, l):
        """Convert HSL to RGB (simplified)"""
        h, s, l = h/360, s/100, l/100
        
        if s == 0:
            r = g = b = l
        else:
            def hue2rgb(p, q, t):
                if t < 0: t += 1
                if t > 1: t -= 1
                if t < 1/6: return p + (q - p) * 6 * t
                if t < 1/2: return q
                if t < 2/3: return p + (q - p) * (2/3 - t) * 6
                return p
            
            q = l * (1 + s) if l < 0.5 else l + s - l * s
            p = 2 * l - q
            
            r = hue2rgb(p, q, h + 1/3)
            g = hue2rgb(p, q, h)
            b = hue2rgb(p, q, h - 1/3)
        
        return int(r * 255), int(g * 255), int(b * 255)
    
    def _get_color_name(self, hex_color):
        """Get a human-readable name for a color"""
        color_names = {
            '#FF0000': 'Red', '#00FF00': 'Green', '#0000FF': 'Blue',
            '#FFFF00': 'Yellow', '#FF00FF': 'Magenta', '#00FFFF': 'Cyan',
            '#000000': 'Black', '#FFFFFF': 'White', '#808080': 'Gray',
            '#FFA500': 'Orange', '#800080': 'Purple', '#FFC0CB': 'Pink',
            '#A52A2A': 'Brown', '#F5F5DC': 'Beige'
        }
        
        # Find the closest named color
        r, g, b = self._hex_to_rgb(hex_color)
        
        min_distance = float('inf')
        closest_name = 'Custom Color'
        
        for named_hex, name in color_names.items():
            nr, ng, nb = self._hex_to_rgb(named_hex)
            distance = math.sqrt((r-nr)**2 + (g-ng)**2 + (b-nb)**2)
            if distance < min_distance:
                min_distance = distance
                closest_name = name
        
        return closest_name

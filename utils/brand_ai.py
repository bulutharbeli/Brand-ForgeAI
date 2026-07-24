import random
import json

class BrandAIGenerator:
    """AI-powered brand generation engine"""
    
    def __init__(self):
        self.industry_prefixes = {
            'technology': ['Tech', 'Cyber', 'Data', 'Cloud', 'Digital', 'Smart', 'AI', 'Next'],
            'healthcare': ['Health', 'Medi', 'Care', 'Life', 'Well', 'Vita', 'Cure', 'Bio'],
            'finance': ['Fin', 'Capital', 'Wealth', 'Money', 'Bank', 'Invest', 'Trade', 'Fund'],
            'education': ['Edu', 'Learn', 'Acad', 'Scholar', 'Study', 'Mind', 'Wise', 'Know'],
            'retail': ['Shop', 'Store', 'Mart', 'Market', 'Buy', 'Style', 'Fashion', 'Trend'],
            'food': ['Food', 'Taste', 'Flavor', 'Fresh', 'Yum', 'Eat', 'Dish', 'Cuisine'],
            'travel': ['Travel', 'Trip', 'Journey', 'Explore', 'Adventure', 'Tour', 'Voyage', 'Go'],
            'fitness': ['Fit', 'Gym', 'Strong', 'Active', 'Power', 'Sport', 'Train', 'Move']
        }
        
        self.industry_suffixes = {
            'technology': ['Ware', 'Logic', 'Labs', 'Systems', 'Solutions', 'Hub', 'Zone', 'Tech'],
            'healthcare': ['Care', 'Health', 'Med', 'Clinic', 'Wellness', 'Life', 'Plus', 'Hub'],
            'finance': ['Capital', 'Finance', 'Invest', 'Wealth', 'Group', 'Partners', 'Advisors', 'Trust'],
            'education': ['Academy', 'Learning', 'Institute', 'Education', 'Hub', 'Center', 'Zone', 'Space'],
            'retail': ['Store', 'Shop', 'Market', 'Mart', 'Boutique', 'Outlet', 'Emporium', 'Co'],
            'food': ['Kitchen', 'Bistro', 'Grill', 'Cafe', 'Eats', 'Foods', 'Restaurant', 'Bar'],
            'travel': ['Travel', 'Tours', 'Air', 'Vacations', 'Explorer', 'Adventures', 'Trips', 'World'],
            'fitness': ['Fitness', 'Gym', 'Training', 'Sports', 'Athletics', 'Performance', 'Lab', 'Zone']
        }
        
        self.slogan_templates = [
            "{{brand}} - {{promise}}",
            "Experience the {{difference}} with {{brand}}",
            "{{brand}}: {{value_proposition}}",
            "Your {{goal}} starts here",
            "{{brand}} - {{action}} your {{outcome}}",
            "Simply {{better_way}}",
            "{{brand}}: Redefining {{industry}}",
            "Unlock your {{potential}} with {{brand}}"
        ]
    
    def generate_brand_names(self, industry, keywords, style='modern'):
        """Generate creative brand names based on industry and keywords"""
        names = []
        
        # Get industry-specific prefixes and suffixes
        prefixes = self.industry_prefixes.get(industry.lower(), ['Pro', 'Smart', 'Prime', 'Ultra'])
        suffixes = self.industry_suffixes.get(industry.lower(), ['Co', 'Labs', 'Hub', 'Zone', 'Works'])
        
        # Generate different types of names
        for _ in range(10):
            name_type = random.choice(['compound', 'portmanteau', 'descriptive', 'abstract', 'founders'])
            
            if name_type == 'compound':
                prefix = random.choice(prefixes)
                suffix = random.choice(suffixes)
                name = f"{prefix}{suffix}"
            
            elif name_type == 'portmanteau' and keywords:
                if len(keywords) >= 2:
                    word1 = keywords[0][:4]
                    word2 = keywords[1][-4:]
                    name = f"{word1}{word2}".capitalize()
                else:
                    name = f"{random.choice(prefixes)}{random.choice(['ly', 'io', 'ai', 'up'])}"
            
            elif name_type == 'descriptive' and keywords:
                keyword = random.choice(keywords).capitalize()
                descriptor = random.choice(['Pro', 'Plus', 'Go', 'Now', 'Lab', 'Hub'])
                name = f"{keyword}{descriptor}"
            
            elif name_type == 'abstract':
                vowels = 'aeiou'
                consonants = 'bcdfghjklmnpqrstvwxyz'
                name = ''
                for i in range(random.randint(5, 8)):
                    if i % 2 == 0:
                        name += random.choice(consonants)
                    else:
                        name += random.choice(vowels)
                name = name.capitalize()
            
            else:  # founders style
                name = f"{random.choice(['The', ''])}{random.choice(prefixes)}{random.choice(['', 'ly', 'io'])}"
                name = name.strip()
            
            # Apply style modifications
            if style == 'modern':
                if random.random() > 0.5:
                    name = name + random.choice(['', 'ly', 'io', 'ai', 'up', 'co'])
            elif style == 'classic':
                name = name + random.choice([' & Sons', ' Group', ' Associates', ' Co.'])
            elif style == 'playful':
                name = name + random.choice(['!', 'y', 'o', 'za'])
            
            if name not in names and len(name) > 2:
                names.append(name)
        
        return names[:10]
    
    def generate_slogans(self, brand_name, industry, values):
        """Generate catchy slogans and taglines"""
        slogans = []
        
        industry_promises = {
            'technology': ['innovation', 'the future', 'digital transformation', 'smart solutions'],
            'healthcare': ['better health', 'wellness', 'care', 'a healthier life'],
            'finance': ['financial freedom', 'wealth', 'security', 'smart investing'],
            'education': ['knowledge', 'learning', 'growth', 'your potential'],
            'retail': ['style', 'quality', 'the best shopping', 'your look'],
            'food': ['great taste', 'freshness', 'delicious meals', 'flavor'],
            'travel': ['adventure', 'discovery', 'unforgettable journeys', 'the world'],
            'fitness': ['strength', 'health', 'your best self', 'peak performance']
        }
        
        promises = industry_promises.get(industry.lower(), ['excellence', 'quality', 'innovation'])
        
        for _ in range(8):
            template = random.choice(self.slogan_templates)
            
            slogan = template.replace('{{brand}}', brand_name)
            slogan = slogan.replace('{{promise}}', random.choice(promises))
            slogan = slogan.replace('{{difference}}', random.choice(['difference', 'future', 'best']))
            slogan = slogan.replace('{{value_proposition}}', f"{random.choice(['The best', 'Premium', 'Innovative'])} {industry}")
            slogan = slogan.replace('{{goal}}', random.choice(['success', 'dreams', 'future']))
            slogan = slogan.replace('{{action}}', random.choice(['Build', 'Create', 'Achieve', 'Transform']))
            slogan = slogan.replace('{{outcome}}', random.choice(['future', 'dreams', 'success']))
            slogan = slogan.replace('{{better_way}}', f"{industry} with {brand_name}")
            slogan = slogan.replace('{{industry}}', industry)
            slogan = slogan.replace('{{potential}}', random.choice(['potential', 'success', 'future']))
            
            if slogan not in slogans:
                slogans.append(slogan)
        
        return slogans
    
    def analyze_brand_voice(self, brand_name, description):
        """Analyze and suggest brand voice/tone"""
        # Simplified analysis based on keywords
        voice_attributes = {
            'professional': ['authoritative', 'expert', 'reliable', 'trustworthy'],
            'friendly': ['warm', 'approachable', 'conversational', 'welcoming'],
            'innovative': ['cutting-edge', 'forward-thinking', 'creative', 'bold'],
            'luxury': ['sophisticated', 'elegant', 'premium', 'exclusive'],
            'playful': ['fun', 'energetic', 'humorous', 'lighthearted'],
            'technical': ['precise', 'detailed', 'informative', 'educational']
        }
        
        # Determine voice based on description keywords
        description_lower = description.lower()
        detected_voice = 'professional'  # default
        
        if any(word in description_lower for word in ['fun', 'play', 'joy', 'happy', 'exciting']):
            detected_voice = 'playful'
        elif any(word in description_lower for word in ['luxury', 'premium', 'exclusive', 'high-end']):
            detected_voice = 'luxury'
        elif any(word in description_lower for word in ['innovative', 'cutting-edge', 'modern', 'future']):
            detected_voice = 'innovative'
        elif any(word in description_lower for word in ['friendly', 'welcoming', 'warm', 'care']):
            detected_voice = 'friendly'
        
        attributes = voice_attributes.get(detected_voice, voice_attributes['professional'])
        
        return {
            'recommended_voice': detected_voice,
            'attributes': attributes,
            'tone_guidelines': self._generate_tone_guidelines(detected_voice),
            'example_phrases': self._generate_example_phrases(detected_voice, brand_name)
        }
    
    def _generate_tone_guidelines(self, voice):
        """Generate tone guidelines based on voice"""
        guidelines = {
            'professional': [
                'Use clear, concise language',
                'Avoid slang and colloquialisms',
                'Maintain formal grammar and punctuation',
                'Focus on expertise and authority'
            ],
            'friendly': [
                'Use conversational language',
                'Address the audience directly',
                'Show empathy and understanding',
                'Be warm and approachable'
            ],
            'innovative': [
                'Use forward-looking language',
                'Emphasize novelty and progress',
                'Be bold and confident',
                'Challenge the status quo'
            ],
            'luxury': [
                'Use sophisticated vocabulary',
                'Emphasize exclusivity and quality',
                'Be refined and elegant',
                'Create aspirational messaging'
            ],
            'playful': [
                'Use humor and wit',
                'Be energetic and fun',
                'Don\'t take yourself too seriously',
                'Engage with creativity'
            ]
        }
        return guidelines.get(voice, guidelines['professional'])
    
    def _generate_example_phrases(self, voice, brand_name):
        """Generate example phrases for the brand voice"""
        examples = {
            'professional': [
                f"At {brand_name}, we deliver excellence.",
                f"Trust {brand_name} for industry-leading solutions.",
                f"Experience the {brand_name} difference."
            ],
            'friendly': [
                f"Hey there! Welcome to {brand_name}!",
                f"We're {brand_name}, and we're so glad you're here!",
                f"Let's do this together with {brand_name}."
            ],
            'innovative': [
                f"{brand_name}: Shaping tomorrow, today.",
                f"Think different. Think {brand_name}.",
                f"The future is {brand_name}."
            ],
            'luxury': [
                f"Experience excellence with {brand_name}.",
                f"{brand_name}: Where luxury meets performance.",
                f"Indulge in the art of {brand_name}."
            ],
            'playful': [
                f"{brand_name}: Where fun happens!",
                f"Life's too short for boring brands. Hello, {brand_name}!",
                f"Get your {brand_name} on!"
            ]
        }
        return examples.get(voice, examples['professional'])
    
    def generate_guidelines(self, brand_name, industry, colors, slogan, voice_tone):
        """Generate comprehensive brand guidelines"""
        return {
            'brand_overview': f"{brand_name} is a {industry} brand focused on delivering exceptional value.",
            'logo_usage': [
                'Always use the approved logo files',
                'Maintain clear space around the logo',
                'Do not stretch or distort the logo',
                'Use appropriate file formats for each medium'
            ],
            'color_usage': {
                'primary': f"Use {colors.get('primary', '#000000')} for main branding elements",
                'secondary': f"Use {colors.get('secondary', '#666666')} for supporting elements",
                'accent': f"Use {colors.get('accent', '#CCCCCC')} sparingly for emphasis"
            },
            'typography': {
                'heading_font': 'Montserrat, sans-serif',
                'body_font': 'Open Sans, sans-serif',
                'note': 'Use web-safe fonts and provide fallbacks'
            },
            'imagery_style': [
                'Use high-quality, professional images',
                'Maintain consistent filter and style',
                'Ensure images align with brand values',
                'Avoid cliché stock photography'
            ],
            'voice_and_tone': voice_tone,
            'do_dont': {
                'do': [
                    'Use the logo consistently',
                    'Follow color palette guidelines',
                    'Maintain brand voice across all communications'
                ],
                'dont': [
                    'Modify the logo without permission',
                    'Use colors outside the palette',
                    'Use inconsistent messaging'
                ]
            }
        }

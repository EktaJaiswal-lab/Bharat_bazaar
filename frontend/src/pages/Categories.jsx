import { Link } from 'react-router-dom';
import { Laptop, Watch, Home as HomeIcon, Sparkles } from 'lucide-react';

const categories = [
  {
    name: 'Electronics',
    icon: <Laptop className="w-12 h-12 mb-4 text-brand-cyan" />,
    description: 'Cyber-decks, drones, and AR gear',
    query: 'Electronics'
  },
  {
    name: 'Wearables & Fashion',
    icon: <Watch className="w-12 h-12 mb-4 text-brand-pink" />,
    description: 'Smart clothing and hover tech',
    query: 'Fashion'
  },
  {
    name: 'Home & Living',
    icon: <HomeIcon className="w-12 h-12 mb-4 text-brand-purple" />,
    description: 'Smart mirrors and ambient lighting',
    query: 'Home'
  },
  {
    name: 'Beauty & Wellness',
    icon: <Sparkles className="w-12 h-12 mb-4 text-white" />,
    description: 'AI skin care and sleep pods',
    query: 'Wellness'
  }
];

export default function Categories() {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 min-h-[80vh]">
      <h1 className="text-4xl md:text-5xl font-bold text-center mb-4">
        Browse by <span className="neon-text">Category</span>
      </h1>
      <p className="text-gray-400 text-center mb-12 max-w-2xl mx-auto">
        Discover the future. Select a category below to explore our cutting-edge AI-curated inventory.
      </p>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {categories.map((cat) => (
          <Link 
            key={cat.name} 
            to={`/products?q=${cat.query}`}
            className="glass-card flex flex-col items-center text-center p-8 group"
          >
            <div className="transform group-hover:scale-110 group-hover:-translate-y-2 transition-all duration-300">
              {cat.icon}
            </div>
            <h3 className="text-xl font-bold mb-2 group-hover:text-brand-cyan transition-colors">{cat.name}</h3>
            <p className="text-sm text-gray-400">{cat.description}</p>
          </Link>
        ))}
      </div>
    </div>
  );
}

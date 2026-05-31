import { Link } from 'react-router-dom';
import { Laptop, Watch, Home as HomeIcon, Sparkles, Gamepad2, Dumbbell, ShoppingBag, UtensilsCrossed, BookOpen, Heart } from 'lucide-react';

const categories = [
  {
    name: 'Electronics',
    icon: <Laptop className="w-12 h-12 mb-4 text-brand-cyan" />,
    description: 'Laptops, drones, cameras & AR gear',
    query: 'Electronics',
    color: 'text-brand-cyan'
  },
  {
    name: 'Wearables',
    icon: <Watch className="w-12 h-12 mb-4 text-brand-pink" />,
    description: 'Smartwatches, fitness bands & VR headsets',
    query: 'Wearables',
    color: 'text-brand-pink'
  },
  {
    name: 'Fashion',
    icon: <ShoppingBag className="w-12 h-12 mb-4 text-yellow-400" />,
    description: 'Clothing, shoes, bags & accessories',
    query: 'Fashion',
    color: 'text-yellow-400'
  },
  {
    name: 'Home & Living',
    icon: <HomeIcon className="w-12 h-12 mb-4 text-brand-purple" />,
    description: 'Decor, lighting, furniture & smart home',
    query: 'Home',
    color: 'text-brand-purple'
  },
  {
    name: 'Gaming',
    icon: <Gamepad2 className="w-12 h-12 mb-4 text-green-400" />,
    description: 'Consoles, controllers, chairs & accessories',
    query: 'Gaming',
    color: 'text-green-400'
  },
  {
    name: 'Beauty',
    icon: <Sparkles className="w-12 h-12 mb-4 text-rose-400" />,
    description: 'Skincare, makeup & hair care tools',
    query: 'Beauty',
    color: 'text-rose-400'
  },
  {
    name: 'Wellness',
    icon: <Heart className="w-12 h-12 mb-4 text-red-400" />,
    description: 'Yoga, massage, supplements & sleep',
    query: 'Wellness',
    color: 'text-red-400'
  },
  {
    name: 'Sports',
    icon: <Dumbbell className="w-12 h-12 mb-4 text-orange-400" />,
    description: 'Cricket, football, gym & outdoor gear',
    query: 'Sports',
    color: 'text-orange-400'
  },
  {
    name: 'Kitchen',
    icon: <UtensilsCrossed className="w-12 h-12 mb-4 text-amber-400" />,
    description: 'Air fryers, coffee makers & cookware',
    query: 'Kitchen',
    color: 'text-amber-400'
  },
  {
    name: 'Books',
    icon: <BookOpen className="w-12 h-12 mb-4 text-sky-400" />,
    description: 'Bestsellers, self-help & business books',
    query: 'Books',
    color: 'text-sky-400'
  },
];

export default function Categories() {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 min-h-[80vh]">
      <h1 className="text-4xl md:text-5xl font-bold text-center mb-4">
        Browse by <span className="neon-text">Category</span>
      </h1>
      <p className="text-gray-400 text-center mb-12 max-w-2xl mx-auto">
        Discover the future. Select a category below to explore our AI-curated inventory.
      </p>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6">
        {categories.map((cat) => (
          <Link
            key={cat.name}
            to={`/products?q=${cat.query}`}
            className="glass-card flex flex-col items-center text-center p-8 group"
          >
            <div className="transform group-hover:scale-110 group-hover:-translate-y-2 transition-all duration-300">
              {cat.icon}
            </div>
            <h3 className={`text-xl font-bold mb-2 group-hover:${cat.color} transition-colors`}>{cat.name}</h3>
            <p className="text-sm text-gray-400">{cat.description}</p>
          </Link>
        ))}
      </div>
    </div>
  );
}

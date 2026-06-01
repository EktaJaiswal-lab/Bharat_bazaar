import { useState, useEffect } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import { Search, ShoppingCart } from 'lucide-react';
import { api } from '../config/api';
import { useCart } from '../context/CartContext';

export default function ProductList() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchParams, setSearchParams] = useSearchParams();
  const [searchQuery, setSearchQuery] = useState(searchParams.get('q') || '');
  const { addToCart } = useCart();

  useEffect(() => {
    const fetchProducts = async () => {
      setLoading(true);
      try {
        const query = searchParams.get('q');
        let url = '/products/?limit=100';
        if (query) {
          url = `/products/search/?q=${encodeURIComponent(query)}`;
        }
        const response = await api.get(url);
        setProducts(response.data);
      } catch (error) {
        console.error("Error fetching products:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, [searchParams]);

  const handleSearch = (e) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      setSearchParams({ q: searchQuery.trim() });
    } else {
      setSearchParams({});
    }
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="flex flex-col md:flex-row justify-between items-center mb-8 gap-4">
        <h1 className="text-4xl font-bold">Explore <span className="neon-text">Products</span></h1>
        
        <form onSubmit={handleSearch} className="relative w-full md:w-96">
          <input 
            type="text" 
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Smart Search (AI Powered)..." 
            className="w-full bg-brand-gray/50 border border-gray-600 rounded-full py-2 pl-4 pr-10 text-white focus:outline-none focus:border-brand-cyan focus:ring-1 focus:ring-brand-cyan transition-all"
          />
          <button type="submit" className="absolute right-3 top-2.5 text-brand-cyan hover:text-white transition-colors">
            <Search className="h-5 w-5" />
          </button>
        </form>
      </div>

      {loading ? (
        <div className="glass p-8 text-center text-brand-cyan rounded-xl animate-pulse">
          Consulting AI for the best products...
        </div>
      ) : products.length === 0 ? (
        <div className="glass p-8 text-center text-gray-400 rounded-xl">
          No products found matching your search.
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {products.map(product => (
            <Link key={product._id} to={`/products/${product._id}`} className="glass-card group flex flex-col h-full overflow-hidden">
              <div className="relative h-48 w-full overflow-hidden">
                <div className="absolute inset-0 bg-brand-cyan/20 group-hover:bg-transparent transition-colors z-10 mix-blend-overlay"></div>
                {product.image_url ? (
                  <img src={product.image_url} alt={product.title} className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"/>
                ) : (
                  <div className="w-full h-full bg-brand-gray flex items-center justify-center text-gray-500">No Image</div>
                )}
              </div>
              <div className="p-4 flex-grow flex flex-col">
                <div className="text-xs text-brand-purple font-semibold uppercase tracking-wider mb-1">{product.category}</div>
                <h3 className="text-lg font-bold text-white mb-1 line-clamp-2">{product.title}</h3>
                <div className="mt-auto pt-4 flex justify-between items-center">
                  <span className="text-xl font-bold neon-text">₹{product.price.toFixed(2)}</span>
                  <button 
                    className="text-white hover:text-brand-cyan transition-colors" 
                    onClick={(e) => {
                      e.preventDefault();
                      addToCart(product);
                    }}
                  >
                    <ShoppingCart className="w-5 h-5" />
                  </button>
                </div>
              </div>
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}

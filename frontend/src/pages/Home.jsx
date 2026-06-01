import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { ArrowRight, Sparkles, ShoppingCart } from 'lucide-react';
import { api } from '../config/api';
import { useCart } from '../context/CartContext';

export default function Home() {
  const [featuredProducts, setFeaturedProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const { addToCart } = useCart();

  useEffect(() => {
    const fetchFeatured = async () => {
      try {
        const mockUserId = localStorage.getItem('user_id') || 'test-user-1';
        // Use the new personalized hybrid endpoint
        const res = await api.get(`/products/recommendations/personalized?user_id=${mockUserId}&limit=3`);
        
        // If it returns nothing (e.g. error fallback), fetch standard
        if (res.data && res.data.length > 0) {
          setFeaturedProducts(res.data);
        } else {
          const fallbackRes = await api.get('/products/?limit=3');
          setFeaturedProducts(fallbackRes.data);
        }
      } catch (err) {
        console.error("Error fetching featured products", err);
        // Fallback
        const fallbackRes = await api.get('/products/?limit=3').catch(e => null);
        if (fallbackRes) setFeaturedProducts(fallbackRes.data);
      } finally {
        setLoading(false);
      }
    };
    fetchFeatured();
  }, []);

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative overflow-hidden pt-20 pb-32">
        {/* Background glow effects */}
        <div className="absolute top-0 left-1/4 w-96 h-96 bg-brand-purple rounded-full mix-blend-multiply filter blur-[128px] opacity-50 animate-blob"></div>
        <div className="absolute top-0 right-1/4 w-96 h-96 bg-brand-cyan rounded-full mix-blend-multiply filter blur-[128px] opacity-50 animate-blob animation-delay-2000"></div>
        <div className="absolute -bottom-32 left-1/2 w-96 h-96 bg-brand-pink rounded-full mix-blend-multiply filter blur-[128px] opacity-50 animate-blob animation-delay-4000"></div>

        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center mt-16">
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full glass border-brand-cyan/30 text-brand-cyan mb-8">
            <Sparkles className="w-4 h-4" />
            <span className="text-sm font-medium tracking-wide uppercase">AI-Powered Shopping</span>
          </div>
          
          <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight mb-8">
            <span className="block text-transparent bg-clip-text bg-gradient-to-r from-brand-cyan to-brand-purple">
              The Future of
            </span>
            <span className="block mt-2">E-Commerce is Here.</span>
          </h1>
          
          <p className="mt-4 max-w-2xl text-xl text-gray-300 mx-auto mb-10">
            Experience hyper-personalized shopping with our Generative AI engine. 
            Discover products you'll love before you even search for them.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link to="/products" className="btn-primary inline-flex items-center justify-center">
              Explore Products <ArrowRight className="ml-2 w-5 h-5" />
            </Link>
            <button className="btn-secondary">
              Chat with AI Assistant
            </button>
          </div>
        </div>
      </section>

      {/* Featured Products */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 relative z-10">
        <div className="flex justify-between items-end mb-8">
          <div>
            <h2 className="text-3xl font-bold tracking-tight">Recommended for You</h2>
            <p className="text-brand-cyan mt-2">Based on your futuristic taste</p>
          </div>
          <Link to="/products" className="text-gray-400 hover:text-white flex items-center transition-colors">
            View All <ArrowRight className="ml-1 w-4 h-4" />
          </Link>
        </div>

        {loading ? (
          <div className="glass p-8 text-center text-brand-cyan rounded-xl animate-pulse">
            Analyzing your preferences...
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {featuredProducts.map(product => (
              <Link key={product._id} to={`/products/${product._id}`} className="glass-card group flex flex-col h-full overflow-hidden">
                <div className="relative h-64 w-full overflow-hidden">
                  <div className="absolute inset-0 bg-brand-cyan/20 group-hover:bg-transparent transition-colors z-10 mix-blend-overlay"></div>
                  {product.image_url ? (
                    <img 
                      src={product.image_url} 
                      alt={product.title} 
                      className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
                    />
                  ) : (
                    <div className="w-full h-full bg-brand-gray flex items-center justify-center text-gray-500">No Image</div>
                  )}
                </div>
                <div className="p-6 flex-grow flex flex-col">
                  <div className="text-xs text-brand-purple font-semibold uppercase tracking-wider mb-2">{product.category}</div>
                  <h3 className="text-xl font-bold text-white mb-2">{product.title}</h3>
                  <div className="mt-auto pt-4 flex justify-between items-center">
                    <span className="text-2xl font-bold neon-text">₹{product.price.toFixed(2)}</span>
                    <button 
                      className="text-white hover:text-brand-cyan transition-colors" 
                      onClick={(e) => {
                        e.preventDefault();
                        addToCart(product);
                      }}
                    >
                      <ShoppingCart className="w-6 h-6" />
                    </button>
                  </div>
                </div>
              </Link>
            ))}
          </div>
        )}
      </section>
    </div>
  );
}

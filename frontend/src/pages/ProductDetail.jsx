import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { ShoppingCart, Star, Sparkles, Heart } from 'lucide-react';
import axios from 'axios';
import { useCart } from '../context/CartContext';

export default function ProductDetail() {
  const { id } = useParams();
  const { addToCart } = useCart();
  const [product, setProduct] = useState(null);
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [isWishlisted, setIsWishlisted] = useState(false);
  const [userRating, setUserRating] = useState(0);

  useEffect(() => {
    const fetchProductData = async () => {
      setLoading(true);
      try {
        const [productRes, recsRes] = await Promise.all([
          axios.get(`http://localhost:8000/products/${id}`),
          axios.get(`http://localhost:8000/products/${id}/similar`)
        ]);
        setProduct(productRes.data);
        setRecommendations(recsRes.data);
        
        // Mock recording a view interaction
        const mockUserId = localStorage.getItem('user_id') || 'test-user-1';
        try {
          // In a real app we'd pass Auth token
          // await axios.post('http://localhost:8000/interactions/', {
          //  user_id: mockUserId, product_id: id, interaction_type: 'view'
          // });
        } catch (e) { console.log(e) }
        
      } catch (error) {
        console.error("Error fetching product data:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchProductData();
    window.scrollTo(0, 0);
  }, [id]);

  const handleRate = (rating) => {
    setUserRating(rating);
    // Mock API call to save rating
    // axios.post('/interactions/', { user_id: 'test', product_id: id, interaction_type: 'rate', rating_value: rating })
  };

  const toggleWishlist = () => {
    setIsWishlisted(!isWishlisted);
    // Mock API call
    // axios.post('/interactions/', { user_id: 'test', product_id: id, interaction_type: 'wishlist' })
  };

  if (loading) {
    return (
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="glass p-8 rounded-xl min-h-[400px] flex items-center justify-center animate-pulse">
          <p className="text-brand-cyan text-xl">Loading product details...</p>
        </div>
      </div>
    );
  }

  if (!product) {
    return (
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="glass p-8 rounded-xl min-h-[400px] flex items-center justify-center">
          <p className="text-red-400 text-xl">Product not found.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      {/* Product Details Section */}
      <div className="glass rounded-2xl overflow-hidden mb-16">
        <div className="grid grid-cols-1 md:grid-cols-2">
          {/* Image */}
          <div className="relative h-96 md:h-full min-h-[400px]">
            {product.image_url ? (
              <img src={product.image_url} alt={product.title} className="absolute inset-0 w-full h-full object-cover" />
            ) : (
              <div className="absolute inset-0 bg-brand-gray flex items-center justify-center text-gray-500">No Image</div>
            )}
            <div className="absolute inset-0 bg-gradient-to-t from-brand-dark to-transparent opacity-60"></div>
            
            <button 
              onClick={toggleWishlist}
              className={`absolute top-6 right-6 p-3 rounded-full glass transition-all duration-300 ${isWishlisted ? 'text-brand-pink bg-brand-pink/20' : 'text-white hover:text-brand-pink'}`}
            >
              <Heart className={`w-6 h-6 ${isWishlisted ? 'fill-current' : ''}`} />
            </button>
          </div>
          
          {/* Info */}
          <div className="p-8 md:p-12 flex flex-col justify-center">
            <div className="text-sm text-brand-purple font-semibold uppercase tracking-wider mb-2">{product.category}</div>
            <h1 className="text-3xl md:text-5xl font-bold mb-4">{product.title}</h1>
            
            <div className="flex items-center space-x-1 text-brand-cyan mb-6">
              {[...Array(5)].map((_, i) => (
                <button key={i} onClick={() => handleRate(i + 1)} className="focus:outline-none hover:scale-110 transition-transform">
                  <Star className={`w-6 h-6 ${(userRating ? i < userRating : i < 4) ? 'fill-current' : 'text-gray-600'}`} />
                </button>
              ))}
              <span className="text-gray-400 text-sm ml-2">({userRating ? 'You rated this' : '42 reviews'})</span>
            </div>
            
            <p className="text-gray-300 text-lg mb-8 leading-relaxed">
              {product.description}
            </p>
            
            <div className="flex flex-wrap gap-2 mb-8">
              {product.tags && product.tags.map(tag => (
                <span key={tag} className="px-3 py-1 bg-brand-gray/50 border border-brand-cyan/30 rounded-full text-xs text-brand-cyan">
                  #{tag}
                </span>
              ))}
            </div>
            
            <div className="flex items-center justify-between mt-auto">
              <span className="text-4xl font-bold neon-text">₹{product.price.toFixed(2)}</span>
              <button 
                onClick={() => addToCart(product)}
                className="btn-primary flex items-center px-8 py-4 text-lg"
              >
                <ShoppingCart className="w-6 h-6 mr-2" /> Add to Cart
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Recommendations Section */}
      {recommendations.length > 0 && (
        <div className="mt-16">
          <div className="flex items-center gap-3 mb-8">
            <Sparkles className="text-brand-purple w-8 h-8" />
            <h2 className="text-3xl font-bold">Similar <span className="neon-text">Products</span></h2>
          </div>
          
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {recommendations.map(rec => (
              <Link key={rec._id} to={`/products/${rec._id}`} className="glass-card group flex flex-col h-full overflow-hidden">
                <div className="relative h-48 w-full overflow-hidden">
                  <div className="absolute inset-0 bg-brand-cyan/20 group-hover:bg-transparent transition-colors z-10 mix-blend-overlay"></div>
                  {rec.image_url ? (
                    <img src={rec.image_url} alt={rec.title} className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"/>
                  ) : (
                    <div className="w-full h-full bg-brand-gray flex items-center justify-center text-gray-500">No Image</div>
                  )}
                </div>
                <div className="p-4 flex-grow flex flex-col">
                  <h3 className="text-lg font-bold text-white mb-1 line-clamp-2">{rec.title}</h3>
                  <div className="mt-auto pt-4 flex justify-between items-center">
                    <span className="text-xl font-bold neon-text">₹{rec.price.toFixed(2)}</span>
                  </div>
                </div>
              </Link>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

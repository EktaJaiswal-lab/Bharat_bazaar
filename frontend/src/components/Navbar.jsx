import { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { ShoppingCart, User, Search, Menu, X, LogOut } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { useCart } from '../context/CartContext';

export default function Navbar() {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  
  const { user, logout } = useAuth();
  const { toggleCart, cartCount } = useCart();
  const navigate = useNavigate();

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 20);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <nav className={`fixed w-full z-50 transition-all duration-300 ${isScrolled ? 'glass py-2' : 'bg-transparent py-4'}`}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center">
          <div className="flex items-center">
            <Link to="/" className="text-2xl font-bold tracking-tighter">
              <span className="text-white">Bharat</span>
              <span className="neon-text">Bazaar</span>
            </Link>
          </div>

          {/* Desktop Menu */}
          <div className="hidden md:flex items-center space-x-8">
            <Link to="/products" className="text-gray-300 hover:text-brand-cyan transition-colors">Products</Link>
            <Link to="/categories" className="text-gray-300 hover:text-brand-cyan transition-colors">Categories</Link>
            <Link to="/dashboard" className="text-gray-300 hover:text-brand-cyan transition-colors">Admin</Link>
            
            <div className="relative">
              <input 
                type="text" 
                placeholder="Search..." 
                className="bg-brand-gray/50 border border-gray-600 rounded-full py-1.5 pl-4 pr-10 text-sm focus:outline-none focus:border-brand-cyan focus:ring-1 focus:ring-brand-cyan transition-all w-64"
              />
              <Search className="absolute right-3 top-1.5 h-4 w-4 text-gray-400" />
            </div>

            <div className="flex items-center space-x-4">
              {user ? (
                <button onClick={handleLogout} className="text-gray-300 hover:text-brand-pink" title="Logout">
                  <LogOut className="h-5 w-5" />
                </button>
              ) : (
                <Link to="/login" className="text-gray-300 hover:text-brand-cyan" title="Login">
                  <User className="h-5 w-5" />
                </Link>
              )}
              
              <button onClick={toggleCart} className="text-gray-300 hover:text-brand-cyan relative">
                <ShoppingCart className="h-5 w-5" />
                {cartCount > 0 && (
                  <span className="absolute -top-2 -right-2 bg-brand-pink text-xs font-bold rounded-full h-4 w-4 flex items-center justify-center">
                    {cartCount}
                  </span>
                )}
              </button>
            </div>
          </div>

          {/* Mobile menu button */}
          <div className="md:hidden flex items-center">
            <button onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)} className="text-gray-300 hover:text-white focus:outline-none">
              {isMobileMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Menu */}
      {isMobileMenuOpen && (
        <div className="md:hidden glass mt-2 p-4 mx-4 rounded-xl absolute w-[calc(100%-2rem)]">
          <div className="flex flex-col space-y-4">
            <Link to="/products" className="text-gray-300 hover:text-brand-cyan transition-colors" onClick={() => setIsMobileMenuOpen(false)}>Products</Link>
            <Link to="/categories" className="text-gray-300 hover:text-brand-cyan transition-colors" onClick={() => setIsMobileMenuOpen(false)}>Categories</Link>
            <Link to="/login" className="text-gray-300 hover:text-brand-cyan transition-colors" onClick={() => setIsMobileMenuOpen(false)}>Login</Link>
            <div className="relative mt-2">
              <input 
                type="text" 
                placeholder="Search..." 
                className="w-full bg-brand-gray/50 border border-gray-600 rounded-full py-2 pl-4 pr-10 text-sm focus:outline-none focus:border-brand-cyan"
              />
              <Search className="absolute right-3 top-2.5 h-4 w-4 text-gray-400" />
            </div>
          </div>
        </div>
      )}
    </nav>
  );
}

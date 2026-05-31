import { X, Plus, Minus, ShoppingBag } from 'lucide-react';
import { useCart } from '../context/CartContext';
import { Link } from 'react-router-dom';

export default function CartSidebar() {
  const { isCartOpen, setIsCartOpen, cartItems, updateQuantity, removeFromCart, cartTotal } = useCart();

  return (
    <>
      {/* Backdrop */}
      {isCartOpen && (
        <div 
          className="fixed inset-0 bg-black/60 backdrop-blur-sm z-40 transition-opacity"
          onClick={() => setIsCartOpen(false)}
        />
      )}

      {/* Sidebar */}
      <div 
        className={`fixed top-0 right-0 h-full w-full sm:w-96 glass border-l border-brand-cyan/20 z-50 transform transition-transform duration-300 ease-in-out flex flex-col ${
          isCartOpen ? 'translate-x-0' : 'translate-x-full'
        }`}
      >
        <div className="p-6 border-b border-white/10 flex justify-between items-center bg-brand-dark/50">
          <h2 className="text-2xl font-bold flex items-center gap-2">
            <ShoppingBag className="text-brand-cyan" /> 
            Your <span className="neon-text">Cart</span>
          </h2>
          <button 
            onClick={() => setIsCartOpen(false)}
            className="p-2 hover:bg-white/10 rounded-full transition-colors"
          >
            <X className="w-6 h-6" />
          </button>
        </div>

        <div className="flex-grow overflow-y-auto p-6 space-y-6">
          {cartItems.length === 0 ? (
            <div className="text-center text-gray-400 mt-10">
              <ShoppingBag className="w-16 h-16 mx-auto mb-4 opacity-20" />
              <p>Your cart is empty.</p>
              <button 
                onClick={() => setIsCartOpen(false)}
                className="mt-4 text-brand-cyan hover:underline"
              >
                Continue Shopping
              </button>
            </div>
          ) : (
            cartItems.map((item) => (
              <div key={item._id} className="flex gap-4 glass p-3 rounded-xl bg-white/5">
                <div className="w-20 h-20 rounded-lg overflow-hidden shrink-0">
                  {item.image_url ? (
                    <img src={item.image_url} alt={item.title} className="w-full h-full object-cover" />
                  ) : (
                    <div className="w-full h-full bg-brand-gray" />
                  )}
                </div>
                <div className="flex flex-col flex-grow">
                  <h3 className="font-semibold text-sm line-clamp-2">{item.title}</h3>
                  <div className="text-brand-cyan font-bold mt-1">₹{item.price.toFixed(2)}</div>
                  
                  <div className="flex items-center justify-between mt-auto pt-2">
                    <div className="flex items-center gap-2 glass rounded-full px-2 py-1 bg-white/5">
                      <button 
                        onClick={() => updateQuantity(item._id, item.quantity - 1)}
                        className="p-1 hover:text-brand-pink transition-colors"
                      >
                        <Minus className="w-3 h-3" />
                      </button>
                      <span className="text-sm w-4 text-center">{item.quantity}</span>
                      <button 
                        onClick={() => updateQuantity(item._id, item.quantity + 1)}
                        className="p-1 hover:text-brand-cyan transition-colors"
                      >
                        <Plus className="w-3 h-3" />
                      </button>
                    </div>
                    <button 
                      onClick={() => removeFromCart(item._id)}
                      className="text-xs text-red-400 hover:text-red-300"
                    >
                      Remove
                    </button>
                  </div>
                </div>
              </div>
            ))
          )}
        </div>

        {cartItems.length > 0 && (
          <div className="p-6 border-t border-white/10 bg-brand-dark/80 backdrop-blur-md">
            <div className="flex justify-between items-center mb-4 text-lg">
              <span className="text-gray-300">Total</span>
              <span className="font-bold text-2xl neon-text">₹{cartTotal.toFixed(2)}</span>
            </div>
            <button className="w-full btn-primary py-4 text-lg font-bold">
              Proceed to Checkout
            </button>
          </div>
        )}
      </div>
    </>
  );
}

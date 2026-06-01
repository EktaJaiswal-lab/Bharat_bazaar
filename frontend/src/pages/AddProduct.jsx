import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '../config/api';
import { PackagePlus, Image as ImageIcon } from 'lucide-react';

export default function AddProduct() {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    price: '',
    category: 'Electronics',
    stock: '',
    image_url: '',
    tags: ''
  });

  const categories = ['Electronics', 'Wearables', 'Fashion', 'Home', 'Beauty', 'Wellness'];

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const productPayload = {
        title: formData.title,
        description: formData.description,
        price: parseFloat(formData.price),
        category: formData.category,
        stock: parseInt(formData.stock),
        image_url: formData.image_url || null,
        tags: formData.tags.split(',').map(tag => tag.trim()).filter(tag => tag !== ''),
        rating: 0.0 // Default rating
      };

      await api.post('/products/', productPayload);
      navigate('/dashboard'); // Go back to dashboard on success
    } catch (err) {
      console.error(err);
      setError('Failed to add product. Please check the inputs.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="flex items-center gap-4 mb-8">
        <PackagePlus className="w-10 h-10 text-brand-cyan" />
        <h1 className="text-4xl font-bold">Add <span className="neon-text">New Product</span></h1>
      </div>

      <div className="glass p-8 rounded-2xl">
        {error && (
          <div className="bg-red-500/20 border border-red-500 text-red-100 p-4 rounded-lg mb-6">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Left Column */}
            <div className="space-y-6">
              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">Product Title</label>
                <input 
                  type="text" 
                  name="title"
                  required
                  value={formData.title}
                  onChange={handleChange}
                  className="w-full bg-brand-gray/50 border border-white/10 rounded-lg p-3 text-white focus:outline-none focus:border-brand-cyan transition-colors" 
                  placeholder="e.g. Neural Link Headset" 
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">Category</label>
                <select
                  name="category"
                  value={formData.category}
                  onChange={handleChange}
                  className="w-full bg-brand-gray/50 border border-white/10 rounded-lg p-3 text-white focus:outline-none focus:border-brand-cyan transition-colors"
                >
                  {categories.map(cat => (
                    <option key={cat} value={cat} className="bg-brand-dark">{cat}</option>
                  ))}
                </select>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">Price (₹)</label>
                  <input 
                    type="number" 
                    name="price"
                    step="0.01"
                    min="0"
                    required
                    value={formData.price}
                    onChange={handleChange}
                    className="w-full bg-brand-gray/50 border border-white/10 rounded-lg p-3 text-white focus:outline-none focus:border-brand-cyan transition-colors" 
                    placeholder="25000" 
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">Initial Stock</label>
                  <input 
                    type="number" 
                    name="stock"
                    min="0"
                    required
                    value={formData.stock}
                    onChange={handleChange}
                    className="w-full bg-brand-gray/50 border border-white/10 rounded-lg p-3 text-white focus:outline-none focus:border-brand-cyan transition-colors" 
                    placeholder="100" 
                  />
                </div>
              </div>
            </div>

            {/* Right Column */}
            <div className="space-y-6">
              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">Description</label>
                <textarea 
                  name="description"
                  required
                  rows="4"
                  value={formData.description}
                  onChange={handleChange}
                  className="w-full bg-brand-gray/50 border border-white/10 rounded-lg p-3 text-white focus:outline-none focus:border-brand-cyan transition-colors" 
                  placeholder="Describe the futuristic features..." 
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">Tags (Comma separated)</label>
                <input 
                  type="text" 
                  name="tags"
                  value={formData.tags}
                  onChange={handleChange}
                  className="w-full bg-brand-gray/50 border border-white/10 rounded-lg p-3 text-white focus:outline-none focus:border-brand-cyan transition-colors" 
                  placeholder="cyberpunk, AI, smart" 
                />
              </div>
            </div>
          </div>

          {/* Full Width Bottom */}
          <div className="pt-4 border-t border-white/10">
            <label className="block text-sm font-medium text-gray-300 mb-2 flex items-center gap-2">
              <ImageIcon className="w-4 h-4" /> Image URL
            </label>
            <input 
              type="url" 
              name="image_url"
              value={formData.image_url}
              onChange={handleChange}
              className="w-full bg-brand-gray/50 border border-white/10 rounded-lg p-3 text-white focus:outline-none focus:border-brand-cyan transition-colors" 
              placeholder="https://images.unsplash.com/..." 
            />
            {formData.image_url && (
              <div className="mt-4 rounded-xl overflow-hidden border border-white/10 h-48 w-full max-w-sm mx-auto">
                <img src={formData.image_url} alt="Preview" className="w-full h-full object-cover" onError={(e) => e.target.style.display = 'none'} />
              </div>
            )}
          </div>

          <div className="pt-6 flex justify-end gap-4">
            <button 
              type="button"
              onClick={() => navigate('/dashboard')}
              className="btn-secondary px-8"
            >
              Cancel
            </button>
            <button 
              type="submit" 
              disabled={loading}
              className="btn-primary px-12"
            >
              {loading ? 'Adding...' : 'Add Product'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

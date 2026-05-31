import { useState } from 'react';
import { RefreshCcw, ShieldCheck, Clock, CheckCircle } from 'lucide-react';

export default function Returns() {
  const [orderId, setOrderId] = useState('');
  const [reason, setReason] = useState('');
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    // Mock API submission
    setTimeout(() => {
      setSubmitted(true);
    }, 1000);
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="text-center mb-16">
        <h1 className="text-4xl md:text-5xl font-bold mb-4">Hassle-Free <span className="neon-text">Returns</span></h1>
        <p className="text-xl text-gray-300 max-w-2xl mx-auto">
          We stand behind our products. If you're not 100% satisfied with your purchase, you can return it within 30 days.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
        <div className="glass p-8 rounded-xl text-center flex flex-col items-center">
          <div className="w-16 h-16 rounded-full bg-brand-cyan/20 flex items-center justify-center mb-6">
            <Clock className="w-8 h-8 text-brand-cyan" />
          </div>
          <h3 className="text-xl font-bold text-white mb-2">30-Day Window</h3>
          <p className="text-gray-400">Return any unused item in its original packaging within 30 days of delivery.</p>
        </div>
        
        <div className="glass p-8 rounded-xl text-center flex flex-col items-center">
          <div className="w-16 h-16 rounded-full bg-brand-purple/20 flex items-center justify-center mb-6">
            <RefreshCcw className="w-8 h-8 text-brand-purple" />
          </div>
          <h3 className="text-xl font-bold text-white mb-2">Instant Processing</h3>
          <p className="text-gray-400">Refunds are processed automatically to your original payment method via our AI backend.</p>
        </div>

        <div className="glass p-8 rounded-xl text-center flex flex-col items-center">
          <div className="w-16 h-16 rounded-full bg-brand-pink/20 flex items-center justify-center mb-6">
            <ShieldCheck className="w-8 h-8 text-brand-pink" />
          </div>
          <h3 className="text-xl font-bold text-white mb-2">No Questions Asked</h3>
          <p className="text-gray-400">We trust you. No long forms or customer service calls required for standard returns.</p>
        </div>
      </div>

      <div className="max-w-2xl mx-auto glass p-8 rounded-2xl relative overflow-hidden">
        <div className="absolute top-0 right-0 w-64 h-64 bg-brand-cyan rounded-full mix-blend-multiply filter blur-[100px] opacity-20"></div>
        
        {submitted ? (
          <div className="text-center py-12">
            <CheckCircle className="w-20 h-20 text-brand-cyan mx-auto mb-6" />
            <h3 className="text-3xl font-bold text-white mb-4">Return Initiated!</h3>
            <p className="text-gray-300 text-lg">
              Your return request for Order #{orderId} has been submitted. Check your email for the return shipping label.
            </p>
            <button onClick={() => setSubmitted(false)} className="mt-8 btn-secondary">
              Submit Another Return
            </button>
          </div>
        ) : (
          <>
            <h2 className="text-2xl font-bold mb-6">Start a Return</h2>
            <form onSubmit={handleSubmit} className="space-y-6 relative z-10">
              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">Order ID</label>
                <input 
                  type="text" 
                  required
                  value={orderId}
                  onChange={(e) => setOrderId(e.target.value)}
                  className="w-full bg-brand-dark/50 border border-gray-600 rounded-lg py-3 px-4 text-white focus:outline-none focus:border-brand-cyan focus:ring-1 focus:ring-brand-cyan"
                  placeholder="e.g. ORD-12345"
                />
              </div>
              
              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">Reason for Return</label>
                <select 
                  required
                  value={reason}
                  onChange={(e) => setReason(e.target.value)}
                  className="w-full bg-brand-dark/50 border border-gray-600 rounded-lg py-3 px-4 text-white focus:outline-none focus:border-brand-cyan focus:ring-1 focus:ring-brand-cyan"
                >
                  <option value="" disabled>Select a reason</option>
                  <option value="wrong_size">Wrong Size</option>
                  <option value="defective">Defective/Damaged</option>
                  <option value="not_as_described">Not as described</option>
                  <option value="changed_mind">Changed my mind</option>
                </select>
              </div>

              <button type="submit" className="w-full btn-primary py-4 text-lg mt-4">
                Generate Return Label
              </button>
            </form>
          </>
        )}
      </div>
    </div>
  );
}

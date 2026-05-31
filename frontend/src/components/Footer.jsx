import { Link } from 'react-router-dom';

export default function Footer() {
  return (
    <footer className="glass mt-12 py-8 border-b-0 border-l-0 border-r-0 rounded-b-none rounded-t-3xl">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row justify-between items-center gap-4">
          <div className="text-center md:text-left">
            <h2 className="text-xl font-bold tracking-tighter">
              <span className="text-white">Bharat</span>
              <span className="neon-text">Bazaar</span>
            </h2>
            <p className="text-gray-400 text-sm mt-2 max-w-sm">
              The futuristic AI-powered e-commerce platform for personalized recommendations.
            </p>
          </div>
          
          <div className="flex space-x-6 text-sm text-gray-400">
            <Link to="/returns" className="hover:text-brand-cyan transition-colors">Return Policy</Link>
            <a href="#" className="hover:text-brand-cyan transition-colors">Privacy Policy</a>
            <a href="#" className="hover:text-brand-cyan transition-colors">Contact</a>
          </div>
        </div>
        
        <div className="mt-8 pt-8 border-t border-gray-800 text-center text-sm text-gray-500">
          &copy; {new Date().getFullYear()} Bharat Bazaar. All rights reserved.
        </div>
      </div>
    </footer>
  );
}

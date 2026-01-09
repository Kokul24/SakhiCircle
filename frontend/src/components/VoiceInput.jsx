/**
 * VoiceInput Component (Simplified)
 * Just a wrapper for textarea now.
 */

import React from 'react';

const VoiceInput = ({ label, value, onChange, placeholder }) => {
  return (
    <div className="w-full">
      <div className="flex justify-between items-center mb-2">
        <label className="block text-sm font-medium text-slate-400">{label}</label>
      </div>
      
      <div className="relative">
        <textarea
          value={value}
          onChange={(e) => onChange(e.target.value)}
          className="w-full bg-slate-800/50 border border-slate-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-blue-500 h-32 resize-none transition-colors"
          placeholder={placeholder}
        />
      </div>
    </div>
  );
};

export default VoiceInput;

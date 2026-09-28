-- Voomi Complete Supabase Schema

CREATE TABLE IF NOT EXISTS public.profiles (
  id UUID PRIMARY KEY,
  email TEXT,
  full_name TEXT,
  avatar_url TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ,
  phone TEXT,
  is_blocked BOOLEAN,
  blocked_at TIMESTAMPTZ,
  username TEXT,
  bio TEXT,
  instagram TEXT,
  tiktok TEXT,
  custom_avatar_url TEXT,
  avatar_description TEXT,
  preferred_name TEXT,
  pov_hand_id UUID,
  custom_pov_hand_url TEXT,
  pov_hand_description TEXT,
  has_seen_onboarding BOOLEAN,
  has_seen_update_video BOOLEAN,
  has_premium_access BOOLEAN,
  has_community_access BOOLEAN,
  premium_expires_at TIMESTAMPTZ,
  community_expires_at TIMESTAMPTZ,
  academy_bonus_redeemed BOOLEAN
);

CREATE TABLE IF NOT EXISTS public.products (
  id UUID PRIMARY KEY,
  name TEXT,
  category TEXT,
  price NUMERIC,
  image_url TEXT,
  sales_count INTEGER,
  rating NUMERIC,
  badge TEXT,
  niche TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  commission_rate INTEGER,
  affiliate_url TEXT,
  target_audience JSONB,
  best_creative_types JSONB,
  avg_daily_sales INTEGER,
  trending_score INTEGER,
  competition_level TEXT,
  profit_margin INTEGER,
  shipping_time TEXT,
  supplier_rating NUMERIC,
  visual_description TEXT,
  display_mode TEXT,
  image_no_bg TEXT
);

CREATE TABLE IF NOT EXISTS public.movement_templates (
  id UUID PRIMARY KEY,
  title TEXT,
  category TEXT,
  prompt TEXT,
  video_url UUID,
  thumbnail_url TEXT,
  sort_order INTEGER,
  is_active BOOLEAN,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  shot TEXT,
  visible_body TEXT,
  product_placement TEXT,
  hands_free BOOLEAN,
  camera TEXT,
  camera_note TEXT,
  beats JSONB,
  motion_clone_enabled BOOLEAN,
  scene_url TEXT
);

CREATE TABLE IF NOT EXISTS public.custom_avatars (
  id UUID PRIMARY KEY,
  user_id UUID,
  name TEXT,
  image_url TEXT,
  description TEXT,
  gender TEXT,
  age_range TEXT,
  hair_color TEXT,
  hair_style TEXT,
  skin_tone TEXT,
  has_beard BOOLEAN,
  beard_style TEXT,
  has_glasses BOOLEAN,
  body_type TEXT,
  extra_traits TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  shirt_color TEXT,
  logo_position TEXT,
  ethnicity TEXT,
  eyebrows TEXT,
  lips TEXT,
  outfit_id UUID
);

CREATE TABLE IF NOT EXISTS public.custom_scenarios (
  id UUID PRIMARY KEY,
  user_id UUID,
  name TEXT,
  image_url TEXT,
  description TEXT,
  scenario_type TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS public.tutorials (
  id UUID PRIMARY KEY,
  title TEXT,
  description TEXT,
  video_url TEXT,
  thumbnail_url TEXT,
  duration_seconds INTEGER,
  category TEXT,
  display_order INTEGER,
  is_published BOOLEAN,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ,
  module_id UUID,
  video_path UUID
);

CREATE TABLE IF NOT EXISTS public.sales (
  id UUID PRIMARY KEY,
  product_id UUID,
  buyer_name TEXT,
  value NUMERIC,
  commission NUMERIC,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  user_id UUID
);

CREATE TABLE IF NOT EXISTS public.sales_aggregates (
  id UUID PRIMARY KEY,
  user_id UUID,
  period_start TIMESTAMPTZ,
  period_end TIMESTAMPTZ,
  total_value INTEGER,
  total_commission INTEGER,
  sales_count INTEGER,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS public.notification_products (
  id UUID PRIMARY KEY,
  user_id UUID,
  product_id UUID,
  custom_product_name TEXT,
  commission_value NUMERIC,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS public.notification_settings (
  id UUID PRIMARY KEY,
  user_id UUID,
  is_active BOOLEAN,
  product_id UUID,
  custom_product_name TEXT,
  commission_value INTEGER,
  min_interval_seconds INTEGER,
  max_interval_seconds INTEGER,
  notification_sound TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS public.ai_generation_costs (
  id UUID PRIMARY KEY,
  user_id UUID,
  kind TEXT,
  status TEXT,
  provider TEXT,
  model_used TEXT,
  cost_usd NUMERIC,
  cost_is_estimated BOOLEAN,
  paid_with TEXT,
  credits_charged INTEGER,
  size TEXT,
  seconds INTEGER,
  ref_id UUID,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS public.user_roles (
  id UUID PRIMARY KEY,
  user_id UUID,
  role TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);


-- Orders & Transactions Table (Checkout & Asaas)
CREATE TABLE IF NOT EXISTS public.orders (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES auth.users(id) ON DELETE SET NULL,
  customer_name TEXT NOT NULL,
  customer_email TEXT NOT NULL,
  customer_phone TEXT,
  customer_cpf TEXT,
  plan_name TEXT NOT NULL,
  amount NUMERIC NOT NULL,
  payment_method TEXT NOT NULL,
  status TEXT DEFAULT 'pending', -- 'pending', 'paid', 'failed', 'refunded'
  asaas_payment_id TEXT,
  pix_qr_code TEXT,
  pix_copy_paste TEXT,
  installments INTEGER DEFAULT 1,
  order_bump BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- RLS (Row Level Security) Configuration
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.products ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.movement_templates ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.tutorials ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.custom_avatars ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.custom_scenarios ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.sales ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.orders ENABLE ROW LEVEL SECURITY;

-- Public read access for catalog items
CREATE POLICY "Public read products" ON public.products FOR SELECT USING (true);
CREATE POLICY "Public read movement_templates" ON public.movement_templates FOR SELECT USING (true);
CREATE POLICY "Public read tutorials" ON public.tutorials FOR SELECT USING (true);

-- User-specific access for profiles
CREATE POLICY "Users can view own profile" ON public.profiles FOR SELECT USING (auth.uid() = id);
CREATE POLICY "Users can update own profile" ON public.profiles FOR UPDATE USING (auth.uid() = id);

-- Orders access
CREATE POLICY "Anyone can insert orders" ON public.orders FOR INSERT WITH CHECK (true);
CREATE POLICY "Users can view own orders" ON public.orders FOR SELECT USING (auth.uid() = user_id OR customer_email = (SELECT email FROM auth.users WHERE id = auth.uid()));

-- Automatically create profile on auth signup
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS trigger AS $$
BEGIN
  INSERT INTO public.profiles (id, email, full_name, avatar_url, created_at, has_premium_access)
  VALUES (
    new.id,
    new.email,
    COALESCE(new.raw_user_meta_data->>'full_name', split_part(new.email, '@', 1)),
    COALESCE(new.raw_user_meta_data->>'avatar_url', ''),
    NOW(),
    TRUE
  )
  ON CONFLICT (id) DO UPDATE
  SET email = EXCLUDED.email;
  RETURN new;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE PROCEDURE public.handle_new_user();
